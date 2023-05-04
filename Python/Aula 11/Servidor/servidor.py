import socket



class Servidor():
    """
    Classe Servidor - API Socket
    """
    def __init__(self, host, port): #param host e porta para falar local
        """
        Construtor da classe servidor
        """
        self._host = host
        self._port = port
    
    def start(self): #normalmente não mexemos no start e no construtor, só no service, o resto é padrão
        """
        Método que inicializa a execução do servidor
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria objeto da classe socket, atribuo ao __tcp
                                                                       #construtor tem parametros (faixa de clientes que podem se conectar, permite escolher qual camada de transporte quer )
                                                                       #AF_INET -> cte da classe que permite qq um conectar ; UDP(socket.SOCKET_DGRAM) ou TCP (socket.SOCKET_STREAM)
        endpoint = (self._host,self._port) #cria endpoint como tupla (imutavel) do servidor (ip,porta) , localiza a aplicação dentro do sistema distribuído
        try:                               #try e except : se acontecer algo de errado no try, execute o except 
            self.__tcp.bind(endpoint)      #vincula o socket ao endpoint (bind)
            self.__tcp.listen(1)           # "escuta", passa flag 1 para executar algo (ir printando )
            #só depois dessa linha o cliente pode se conectar

            print("Servidor iniciado em ",self._host,": ", self._port)
            while True:                           #loop continuo
                con, client = self.__tcp.accept() #accept , !!COMANDO BLOQUEANTE!! (código do servidor fica parado na linha 27)
                                                  #recebo uma tupla, representando a conexão e endereço do cliente 
                self._service(con,client)         #executo o serviço (que eu irei programar) a executar
        except Exception as e:            #tipo da execeção como 'e' // Exception é a mais geral, mas temos ConectionError, etc etc (ver doc do bind)
            print("Erro ao inicializar o servidor",e.args)
    
    def _service(self, con, client):       #método do serviço
        """
        Método que implementa o serviço de calculadora
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True:
            try: 
                msg = con.recv(1024)              #receive , COMANDO BLOQUEANTE fica travado até cliente mandar algo, recebe mensagem do cliente 1024 é tamanho do pacote que quero receber
                msg_s = str(msg.decode('ascii'))  #decodifica mensagem que está em bytes para string, varia de acordo com protocolo de comunicação (no caso "5+3+8") 
                resp = eval(msg_s)                #recebe string e executa no python "basicamente" (se manda print ele printa)
                con.send(bytes(str(resp),'ascii')) #envia a resposta como bytes(codifica resposta para bytes de acordo com ascii)
                print(client," -> requisição atendida") 
            except OSError as e:                  #caso erro de conexão com cliente
                print("Erro de conexão ",client,": ",e.args)
                return  
            except Exception as e:                #caso erro geral
                print("Erro nos dados recebidos pelo cliente ",client,": ",e.args)
                con.send(bytes("Erro",'ascii'))
                return
