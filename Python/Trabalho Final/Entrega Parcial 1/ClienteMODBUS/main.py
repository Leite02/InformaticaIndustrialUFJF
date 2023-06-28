from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from pyModbusTCP.client import ModbusClient
from threading import Thread
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian


class MyWidget(BoxLayout):  # é o raiz da aplicação
    def connect(self):
        ip_server = self.ids.ip.text
        port_server = int(self.ids.port.text)
        self._cliente = ModbusClient(host=ip_server, port=port_server)
        self._scan_time = 1.0
        self._cliente.open()
        self.ids.titulo_conectado.text = "Conexão estabelecida"
        self._ev = Clock.schedule_interval(self.atendimentoRepeat, self._scan_time)

    def leDadoHolding(self, addr, div):
        leitura_noDiv = self._cliente.read_holding_registers(addr, 1)[0]
        leitura_Holding = int(leitura_noDiv) / div
        return str(leitura_Holding)

    def leDadoFP(self, addr):
        leitura_cod = self._cliente.read_holding_registers(addr, 2)
        #byteorder BIG wordorder LITTLE
        decoder = BinaryPayloadDecoder.fromRegisters(leitura_cod, byteorder=Endian.Big, wordorder=Endian.Little)
        leitura_FP = str(round(decoder.decode_32bit_float(), 2))
        return leitura_FP

    def leDadoValvula(self, addr, bit):
        leitura_v = self._cliente.read_holding_registers(addr, 1)[0]
        lista_bits = [int(x) for x in "{0:016b}".format(leitura_v)]
        return str(lista_bits[abs(15 - bit)])

    def checkValvula(self, valvula):
        if valvula == "1":
            valvula = "Aberta"
            return valvula
        elif valvula == "0":
            valvula = "Fechada"
            return valvula

    def atendimentoRepeat(self, dt):
        try:
            valvula1 = self.checkValvula(self.leDadoValvula(712, 0))
            valvula2 = self.checkValvula(self.leDadoValvula(712, 1))
            valvula3 = self.checkValvula(self.leDadoValvula(712, 2))
            valvula4 = self.checkValvula(self.leDadoValvula(712, 3))
            valvula5 = self.checkValvula(self.leDadoValvula(712, 4))
            valvula6 = self.checkValvula(self.leDadoValvula(712, 5))

            pit_01 = self.leDadoFP(714)
            fit_02 = self.leDadoFP(716)
            fit_03 = self.leDadoFP(718)

            torque = self.leDadoFP(1420)
            velocidade = self.leDadoFP(884)
            corrente_med = self.leDadoHolding(845, 10)

            self.ids.leituraUm.text = valvula1
            self.ids.leituraDois.text = valvula2
            self.ids.leituraTres.text = valvula3
            self.ids.leituraQuatro.text = valvula4
            self.ids.leituraCinco.text = valvula5
            self.ids.leituraSeis.text = valvula6
            self.ids.leituraSete.text = pit_01
            self.ids.leituraOito.text = fit_02
            self.ids.leituraNove.text = fit_03
            self.ids.leituraDez.text = torque
            self.ids.leituraOnze.text = velocidade
            self.ids.leituraDoze.text = corrente_med

        except Exception as e:
            print("Erro no atendimento: ", e.args)


class ClienteMod(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """

        return MyWidget()


if __name__ == "__main__":
    Window.size = (800, 600)  # tamanho da janela desejado
    Window.fullscreen = False  # inicializa sem ser fullscreen
    ClienteMod().run()
