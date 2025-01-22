import socket
import cv2
import os
import numpy as np


class Servidor():
    """
    Classe Servidor - API Socket
    """
    def __init__(self, host, port): #param host e porta para falar local
        """
        Construtor da classe servidor
        """
        self._host = host                                                #cria objeto da classe socket, atribuo ao __tcp
        self._port = port                                                #construtor tem parametros (faixa de clientes que podem se conectar, permite escolher qual camada de transporte quer )
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #AF_INET -> cte da classe que permite qq um conectar (familia de protocolo IP); Protocolo usado: UDP(socket.SOCKET_DGRAM) ou TCP (socket.SOCKET_STREAM) ->camada de transporte 
           
         

    def start(self): #normalmente não mexemos no start e no construtor, só no service, o resto é padrão
        """
        Método que inicializa a execução do servidor
        """
        endpoint = (self._host,self._port) #cria endpoint como tupla (imutavel) do servidor (ip,porta) , localiza a aplicação dentro do sistema distribuído
        try:                               #try e except : se acontecer algo de errado no try, execute o except 
            self.__tcp.bind(endpoint)      #vincula o socket ao endpoint (bind)
            self.__tcp.listen(1)           # "escuta", passa flag 1 para executar algo (ir printando )
            #só depois dessa linha o cliente pode se conectar

            print("Servidor iniciado em ",self._host,": ", self._port)
            while True:                           #loop continuo
                con, client = self.__tcp.accept() #accept , !!COMANDO BLOQUEANTE!! (código do servidor fica parado na linha 27, até um cliente conectar)
                                                  #recebo uma tupla, representando a conexão e endereço do cliente 
                self._service(con,client)         #executo o serviço (que eu irei programar) a executar
        except Exception as e:            #tipo da execeção como 'e' // Exception é a mais geral, mas temos ConectionError, etc etc (ver doc do bind)
            print("Erro ao inicializar o servidor",e.args)
    
    def _service(self, con, client):       #método do serviço
        """
        Método que implementa o serviço de calculadora
        :param con: objeto socket utilizado para enviar e receber dados(vai ter ip e porta do cliente)
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True:
            try: 
                tamanho_da_imagemrecebida_codificado = con.recv(1024) #receive , COMANDO BLOQUEANTE fica travado até cliente mandar algo, recebe mensagem do cliente 1024 é tamanho do pacote que quero receber
                tamanho_da_imagemrecebida = int.from_bytes(tamanho_da_imagemrecebida_codificado,'big')
                
                img_recebida_bytes = con.recv(1024)
                tamanho_recebido_codificado = len(img_recebida_bytes).to_bytes(4,'big')
                tamanho_recebido = int.from_bytes(tamanho_recebido_codificado,'big')
                while tamanho_recebido < tamanho_da_imagemrecebida:
                    img_recebida_bytes += con.recv(1024)
                    tamanho_recebido_codificado = len(img_recebida_bytes).to_bytes(4,'big')
                    tamanho_recebido = int.from_bytes(tamanho_recebido_codificado,'big')
                
                img = cv2.imdecode(np.frombuffer(img_recebida_bytes, np.uint8), cv2.IMREAD_COLOR)

                # processamento
                xml_classificador = os.path.join(os.path.relpath(
                    cv2.__file__).replace('__init__.py', ''), 'data\haarcascade_frontalface_default.xml')
                face_cascade = cv2.CascadeClassifier(
                    xml_classificador)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                # Desenha retângulos nas áreas onde as faces foram detectadas
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                _, img_bytes = cv2.imencode('.jpg', img)
                img_bytes = bytes(img_bytes)
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
                con.send(tamanho_da_imagem_codificado)
                con.send(img_bytes)
                
                print("Tamanho da imagem: ",tamanho_da_imagemrecebida)
                print(client," -> requisição atendida") 
            except OSError as e:                  #caso erro de conexão com cliente
                print("Erro de conexão ",client,": ",e.args)
                return  
            except Exception as e:                #caso erro geral
                print("Erro nos dados recebidos pelo cliente ",client,": ",e.args)
                con.send(bytes("Erro",'ascii'))
                return