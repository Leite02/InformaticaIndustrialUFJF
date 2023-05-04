import socket

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
                msg = input("Digite a operação (x para sair): ") #pede para inserir a mensagem
                if msg == '':
                    continue
                elif msg == 'x': #se mensagem for x saia do loop e encerra serviço
                    break
                self.__tcp.send(bytes(msg,'ascii')) #manda a mensagem em bytes
                resp = self.__tcp.recv(1024)        #recebe a resposta do servidor com max de 1024
                print("= ",resp.decode('ascii'))    #printa a resposta decodificando os bytes
            self.__tcp.close()                      #fecha conexão  
        except Exception as e:                      #caso erro
            print("Erro ao realizar comunicação com o servidor", e.args)
