import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class BasicApp(App):  # cria classe BasicApp a partir da classe App básica (herança)
    """
    Aplicativo básico Kivy
    """

    def build(self,):  # todas classes criadas devem ter o build(), método básico, tem q retornar o widget root (layout)
        """
        Constrói o aplicativo a partir de um conjunto de widgets
        :return Widget principal da aplicação
        """
        layout = BoxLayout(orientation="horizontal")  # criando um BoxLayout(do kivy já); permite adicionar outros componentes
        # e serão organizados automaticamente na horizontal
        self.lb = Label(text="0")  # criando um rótulo (label), passamos para o atributo lb, ele criaria uma caixinha
        # com o texto "0"
        bt = Button(text="Botão 1", on_release=self.incrementar)  # criando um botão um botão com texto "Botão 1"
                                                                  #asssociamos um método incrementar ao EVENTO on_release
                                                                  #ou seja, ao soltar o botão, executa o método passado
                                                                  
        layout.add_widget(self.lb)  # adiciona o label (atributo lb da classe) no layout
        layout.add_widget(bt)  # adiciona o botão (variavel bt) no layout

        layout2 = BoxLayout(orientation="vertical")  # criando outro layout, mas que vai organizar verticalmente
        self.lb2 = Label(text="0", color=[1, 0, 0, 1])  # criando outro label no atributo lb2; color = [R,G,B,saturação]
        self.lb3 = Label(text="0")  # criando outro label no atributo lb3
        layout2.add_widget(self.lb2)  # adiciona label2 no layout2
        layout2.add_widget(self.lb3)  # adiciona label3 no layaout2
        layout.add_widget(layout2)  # adiciona o layout2 no layout original

        return layout  # retorna o layout original (será o raiz)

    def incrementar(self, *args):  # cria um método incrementar
        #o args é uma lista, que permite passar depois de definido, quantos argumentos eu quiser
            #declarar de maneira genérica os argumentos de uma função/método
            #existe o **kwargs (key word args), passamos o args como parâmetros nominais (dicionario)
            #como se ao chamar a função eu fizesse incrementar(arg1=30,tam=20,...)
            
        #passa valor p/ int, soma e dps volta p/ string
        self.lb.text = str(int(self.lb.text) + 1)  # incrementa o texto do atributo lb
        self.lb2.text = str(int(self.lb2.text) + 2)  # incrementa o texto do atributo lb2
        self.lb3.text = str(int(self.lb3.text) + 3)  # incrementa o texto do atributo lb3


if __name__ == "__main__":
    BasicApp().run()
