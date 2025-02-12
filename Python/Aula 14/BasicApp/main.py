import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class MyWidget(BoxLayout): #cria uma classe derivada do BoxLayout
    def changelb(self):
        """
        Método simples para incremento do valor mostrado no label
        """
        self.ids['lb'].text = str(int(self.ids.lb.text) + 1)  #self.ids é um dicionario de todos os ids dos componentes dentro da classe
                                                              #acessa o componente pelo id

class BasicApp(App): #cria a classe BasicApp pela herança
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget() #retorna o layout MyWidget criado por herança do BoxLayout
 
if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    BasicApp().run()