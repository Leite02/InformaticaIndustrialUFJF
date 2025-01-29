from pyModbusTCP.server import DataBank, ModbusServer
import random
from time import sleep


class ServidorMODBUS():
    """
    Classe Servidor Modbus
    """
    
    def __init__(self, host_ip, port): #passa ip e porta, na qual oferecemos o serviço de dados MODBUS
        """
        Construtor
        """
        self._db = DataBank() #objeto que guarda a tabela de dados do modbus, bobinas, etc etc
        self._server = ModbusServer(host=host_ip,port=port,no_block=True,data_bank=self._db) #cria objeto servidor 
        #com todas subrotinas do MODBUS (parecido com objeto da api socket)(não precisa referenciar bind etc...)
        #além disso, adicionamos o no_block = True (já cria servidor MultiThread, atende múltiplos clientes)
        #e passamos o databank criado
        
    def run(self):  #método START
        """
        Execução do servidor Modbus
        """
        try:
            self._server.start() #da start
            print("Servidor MODBUS em execução")
            while True: #vai colocar dados randomicos (como se fosse o clp com dados armazenados)
                self._db.set_holding_registers(1000,[random.randrange(int(0.95*400),int(1.05*400))]) #coloca no holding de endereço 1000 um valor random, que varia nesse caso de 380 a 420
                print('======================')
                print("Tabela MODBUS")
                print(f'Holding Register \r\n R1000: {self._db.get_holding_registers(1000)} \r\n R2000: {self._db.get_holding_registers(2000)}') #le valores do holding nos endereços 1000 e 2000
                print(f'Coil \r\n R1000: {self._db.get_coils(1000)}') #le valor de Coil no endereço 1000
                #podemos ter dado no msm endereço, se forem diferentes, estarão em tabelas diferentes, entao ok
                sleep(1)
        except Exception as e:
            print("Erro: ",e.args)



    

