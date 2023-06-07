from pyModbusTCP.client import ModbusClient
from time import sleep
from dbhandler import DBHandler
from datetime import datetime
from threading import Thread
from tabulate import tabulate

class ModbusPersistencia(object):
    """
    Classe que implementa funcionalidade de persistência de dados 
    lidos a partir do protocolo Modbus e também permite a busca de dados históricos
    """
    def __init__(self, server_ip,porta, tags_addrs, scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip, port=porta)
        self._scan_time = scan_time                               #de quanto em quanto tempo busca infos no servidor
        self._tags_addrs = tags_addrs                             #armazena tags
        self._dbclient = DBHandler('data\data.db',self._tags_addrs.keys(),'modbusData') #cliente database (especificar certo o arquivo)
        self._threads = []                                        #lista de threads p/ 3 tarefas q teremos
                                                                  #buscar info servidor
                                                                  #armazenar database
                                                                  #fazer ihm dados históricos c input (SERÁ BLOQUEANTE ESSA)
                                                                  #por isso precisamos de múltiplas threads

    def guardar_dados(self):
        """
        Método para leitura de um dado da tabela MODBUS
        """
        try:
            print("Persistência iniciada")
            self._cliente.open()               #abre comunicação com servidor
            data = {}                          #cria dicionario vazio
            
            #fica rodando o while True pra ficar atualizando sempre a leitura e armazenando, a partir de uma chamada
            #no tempo do scantime
            while True:
                data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")  #adiciona a data de agora no 'timestamp'
                for tag in self._tags_addrs:         #para tag nas tags que temos
                    #adiciona no dicionário data com a chave tag ('temperatura','pressao',etc)
                    #o valor da leitura la no servidor da tag a partir do valor atribuido a chave tag(1001,1002,etc)
                    data[tag]= self._cliente.read_holding_registers(self._tags_addrs[tag],1)[0]
                
                #pede ao dbclient pra inserir os dados coletados no database que estavam no dicionario data 
                self._dbclient.insert_data(data)
                sleep(self._scan_time) #sleep pelo scantime

        except Exception as e:
            print("Erro na persistência dos dados: ", e.args)

    def acesso_dados_historicos(self): #HISTORIADOR
        """
        Método que permite ao usuário acessar dados históricos
        """
        try:
            print("Bem vindo ao sistema de busca de dados históricos")
            
            #roda p/ sempre pra pegar dados que quiserem passar (por isso importante ter a thread)
            while True:
                #pega o horario inicial no formato especificado
                init = input("Digite o horário inicial para a busca (DD/MM/AAAA HH:MM:SS):")
                #pega o horario final no formato especificado
                final = input("Digite o horário final para a busca (DD/MM/AAAA HH:MM:SS):")
                #converte do formato especificado para o necessário p/ sql
                init = datetime.strptime(init, '%d/%m/%Y %H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")
                final = datetime.strptime(final, '%d/%m/%Y %H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")
                #armazena o resultado coletado do dbclient a partir do init e final
                result = self._dbclient.select_data(self._tags_addrs.keys(), init, final)
                #printa p/ usuário usando tabulate pra ficar mais bunitin
                print(tabulate(result['data'], headers=result['cols']))


        except Exception as e:
            print("Erro: ", e.args)

    def run(self):
        self._threads.append(Thread(target=self.guardar_dados))
        self._threads.append(Thread(target=self.acesso_dados_historicos))
        for t in self._threads:
            t.start()

    
