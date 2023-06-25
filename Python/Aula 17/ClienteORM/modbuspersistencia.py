from pyModbusTCP.client import ModbusClient
from time import sleep
from datetime import datetime
from threading import Thread
from threading import Lock
from tabulate import tabulate
from db import Base,Session,engine
from models import DadoCLP

class ModbusPersistencia(object):
    """
    Classe que implementa funcionalidade de persistência de dados 
    lidos a partir do protocolo Modbus
    """
    def __init__(self, server_ip,porta, tags_addrs, scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip, port=porta)
        self._scan_time = 1
        self._tags_addrs = tags_addrs
        self._session = Session()
        Base.metadata.create_all(engine)
        self._threads = []
        self._lock = Lock()

    def guardar_dados(self):
        """
        Método para leitura de um dado da tabela MODBUS
        """
        try:
            print("Persistência iniciada")
            self._cliente.open()
            data = {}
            while True:
                data['timestamp'] = datetime.now()
                #leio os dados do servidor modbus e guardo no data
                for tag in self._tags_addrs:
                    data[tag]= self._cliente.read_holding_registers(self._tags_addrs[tag], 1)[0]
                
            #o ** é um dict unpacking, o 'data' é um dicionario c 5 chaves, o que o dict unpacking faz é:
            # DadoCLP(timestamp=data['timestamp'],temperatura=data['temperatura],......)
            #pega o dicionário e abre ele, no nosso caso já passando como parametros
            
                dado = DadoCLP(**data) #crio objeto dado a partir da classe DadoCLP que possui os dados da leitura
                self._lock.acquire() #acquire do Lock
                self._session.add(dado) #adiciona na sessão, para ser mudada na tabela
                self._session.commit() #comita as mudanças adicionas na sessão p/ realmente mudar
                self._lock.release() #solta o Lock
                sleep(self._scan_time)

        except Exception as e:
            print("Erro na persistência dos dados: ", e.args)

    def acesso_dados_historicos(self):
        """
        Método que permite ao usuário acessar dados históricos
        """
        try:
            print("Bem vindo ao sistema de busca de dados históricos")
            while True:
                init = input("Digite o horário inicial para a busca (DD/MM/AAAA HH:MM:SS):") #pega hora inicial
                final = input("Digite o horário final para a busca (DD/MM/AAAA HH:MM:SS):") #pega hora final
                init = datetime.strptime(init, '%d/%m/%Y %H:%M:%S') #formata o init
                final = datetime.strptime(final, '%d/%m/%Y %H:%M:%S') #formata o final
                self._lock.acquire() #bloqueia o Lock
                results = self._session.query(DadoCLP).filter(DadoCLP.timestamp.between(init,final)).all() #lê dados da tabela a partir do init e final estabelecidos
                self._lock.release() #libera o lock
                results_fmt_lst = [reg.get_attr_printable_list() for reg in results] #formata os dados p/printar
                print(tabulate(results_fmt_lst,headers=DadoCLP.__table__.columns.keys())) #printa na tela
        except Exception as e:
            print("Erro: ", e.args)

    def run(self):
        self._threads.append(Thread(target=self.guardar_dados))
        self._threads.append(Thread(target=self.acesso_dados_historicos))
        for t in self._threads:
            t.start()

    
