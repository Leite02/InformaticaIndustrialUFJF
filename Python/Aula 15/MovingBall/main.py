from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from time import sleep

class MyWidget(BoxLayout): #é o raiz da aplicação
    _vel = [1,1]           #atributo protegido da velocidade -> [velx, vely]

    def move(self,dt): #método do movimento
        self.ids.bola.x += self._vel[0]  #adiciono na coordenada x do canto inferior esquerdo o valor velx
        self.ids.bola.y += self._vel[1]  #adiciono na coordenada y do canto inferior esquerdo o valor vely
        if self.ids.bola.x < 0 or self.ids.bola.right > self.ids.valid_region.width: #se a bola for vazar pelo x ou o lado direito pelo lado max do RelativeLayout
            self._vel[0] *= -1  #altera o sinal da velx
        if self.ids.bola.y < 0 or self.ids.bola.top > self.ids.valid_region.height: #se a bola for vazar pelo y ou o lado do topo pelo topo max do RelativeLayout
            self._vel[1] *= -1  #altera o sinal da vely

      
    def command(self): #método de comando do botão (botão tem função dupla, em momentos distintos)
        if self.ids.bt_mover.text == "Mover": #se botao tiver com o texto mover
            self._ev = Clock.schedule_interval(self.move, 1.0/60.0) #agenda o evento de mover c tempo de 1/60 (60x por segundo q executa)
            self.ids.bt_mover.text = "Parar" #muda o texto do botao para parar
        elif self.ids.bt_mover.text == "Parar": #se o botao tiver com o texto mover
            self._ev.cancel() #cancela o evento agendado
            self.ids.bt_mover.text = "Mover" #muda o texto do botao para mover

class MovingBallApp(App): #cria a classe MovingBallApp derivada de App
    def build(self): #método inicial de build
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget() #retorna widget raiz

if __name__ == '__main__':
    Window.size = (800,600) #tamanho da janela desejado
    Window.fullscreen = False #inicializa sem ser fullscreen
    MovingBallApp().run()