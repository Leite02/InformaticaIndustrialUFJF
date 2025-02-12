import socket
import cv2
import os
import numpy as np

class Cliente():
    """
    Classe Cliente - API Socket
    """
    def __init__(self, server_ip, port):  #construtor, passo ip do servidor e porta
        """
        Construtor da classe Cliente
        """
        self.__server_ip = server_ip
        self.__port = port
    
    def start(self):
        """
        Método que inicializa a execução do Cliente
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crio objeto do tipo socket
        endpoint = (self.__server_ip,self.__port) #crio o endpoint
        try:
            self.__tcp.connect(endpoint) #conecto com servidor
            print("Conexão realizada com sucesso!")
            self.__method() #chamo método do cliente
        except:
            print("Servidor não disponível")

    
    def __method(self): #implemento o método
        """
        Método que implementa as requisições do cliente
        """
        try:
            msg = ''  #cria mensagem como string vazia
            while msg != '\x18':  #enquanto a mensagem não for o caracterere \x18 da ascii
                msg = input("Digite o numero final da imagem (x para sair): ") #pede para inserir a mensagem
                if msg == '':
                    continue
                elif msg == 'x': #se mensagem for x saia do loop e encerra serviço
                    break
                caminho_imagem = 'faces/image_000' + msg + '.jpg'
                img = cv2.imread(caminho_imagem)
                # codificação para bytes
                _, img_bytes = cv2.imencode('.jpg', img)
                img_bytes = bytes(img_bytes)
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')

                self.__tcp.send(tamanho_da_imagem_codificado) #manda um numero referente ao tamanho
                self.__tcp.send(img_bytes)                    #manda os bytes da

                tamanho_da_imagemrecebida_codificado = self.__tcp.recv(1024) #recebe a resposta do servidor com max de 1024(string)
                tamanho_da_imagemrecebida = int.from_bytes(tamanho_da_imagemrecebida_codificado, "big")

                img_recebida_bytes = self.__tcp.recv(1024)
                tamanho_recebido_codificado = len(img_recebida_bytes).to_bytes(4, "big")
                tamanho_recebido = int.from_bytes(tamanho_recebido_codificado, "big")
                
                while tamanho_recebido < tamanho_da_imagemrecebida:
                    img_recebida_bytes += self.__tcp.recv(1024)
                    tamanho_recebido_codificado = len(img_recebida_bytes).to_bytes(4, "big")
                    tamanho_recebido = int.from_bytes(tamanho_recebido_codificado, "big")

                img = cv2.imdecode(np.frombuffer(img_recebida_bytes, np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow('Imagem Processada', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            self.__tcp.close()                      #fecha conexão  
        except Exception as e:                      #caso erro
            print("Erro ao realizar comunicação com o servidor", e.args)
