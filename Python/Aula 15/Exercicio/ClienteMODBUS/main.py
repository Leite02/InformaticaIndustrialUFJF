from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

# from pyModbusTCP.client import ModbusClient


class MyWidget(BoxLayout):  # é o raiz da aplicação
    def connect(self):
        pass

    # ip_server = self.root.ids.ip.text
    # port_server = self.root.ids.port.text
    # self._cliente = ModbusClient(host = ip_server, port = port_server)
    # self._scan_time = 1./30.
    # self._cliente.open()

    # def changeSelAddr(self,text,address):
    #   self._sel = text
    #  self._addr = address

    # def atendimento(self):
    #   self._cliente.open()
    #  try:
    #     atendimento = True
    #    while atendimento:
    #       if self._sel == '1':


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
