import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


class MyWidget(BoxLayout):  # cria uma classe derivada do BoxLayout
    def changelb(self,adicionar):
        """
        Método simples para incremento do valor mostrado no label
        """
        if self.ids["value"].text == '0':
            self.ids["value"].text = str(adicionar)
        else:
            self.ids["value"].text = str(
                self.ids.value.text + str(adicionar)
            )  # self.ids é um dicionario de todos os ids dos componentes dentro da classe
            # acessa o componente pelo id
    
    def equal(self):
        self.ids["value"].text = str(eval(self.ids["value"].text))
    
    def delete(self):
        self.ids["value"].text = self.ids["value"].text[:-1]
    
    def clear(self):
        self.ids["value"].text = '0'


class BasicApp(App):  # cria a classe BasicApp pela herança
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()  # retorna o layout MyWidget criado por herança do BoxLayout


if __name__ == "__main__":
    Config.set("graphics", "resizable", True)
    BasicApp().run()
