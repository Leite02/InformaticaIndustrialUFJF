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
        self._scan_time = 1
        self._cliente.open()
        self.ids.leitura.text = "Conexão estabelecida"

    def changeSelAddr(self, text, address):
        self._sel = text
        self._addr = int(address)
        if self.ids.checkbox.active:
            self._ev = Clock.schedule_interval(
                self.atendimentoRepeat, self._scan_time
            )  # ver na aula como melhorar o lag com multithreading
        else:
            self._ev = Clock.schedule_once(self.atendimentoRepeat)

    def atendimentoRepeat(self, dt):
        try:
            if self._sel == "1":
                self.ids.leitura.text = str(
                    self._cliente.read_holding_registers(self._addr, 1)[0]
                )

            elif self._sel == "2":
                leitura = self._cliente.read_holding_registers(self._addr,2)
                decoder = BinaryPayloadDecoder.fromRegisters(leitura,byteorder=Endian.Big,wordorder=Endian.Big)
                self.ids.leitura.text = str(decoder.decode_32bit_float())

            elif self._sel == "3":
                leitura = self._cliente.read_holding_registers(self._addr,1)[0]
                lista_bits = [int(x) for x in '{0:016b}'.format(leitura)]
                self.ids.leitura.text = str(lista_bits)

            elif self._sel == "4":
                self.ids.leitura.text = str(
                    self._cliente.read_input_registers(self._addr, 1)[0]
                )

            if not self.ids.checkbox.active:
                self._ev.cancel()

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
