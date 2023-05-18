from pyModbusTCP.client import ModbusClient
from time import sleep

class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """
    def __init__(self, server_ip,porta,scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip,port = porta) #cria objeto cliente modbus com ip e porta determinados
        self._scan_time = scan_time  #seta periodo em que "pergunta" para coletar dados

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        self._cliente.open() #faz a conexão com o servidor
        try:
            atendimento = True  #tipo atendimento do banco
            while atendimento:
                sel = input("Deseja realizar uma leitura, escrita ou configuração? (1- Leitura | 2- Escrita | 3- Configuração |4- Sair): ")
                
                if sel == '1':
                    tipo = input ("""Qual tipo de dado deseja ler? (1- Holding Register |2- Coil |3- Input Register |4- Discrete Input) :""") #pega o tipo de dado a ler
                    addr = input (f"Digite o endereço da tabela MODBUS: ") #pega o endereço de leitura
                    nvezes = input ("Digite o número de vezes que deseja ler: ") #pega o nvezes que quer ler
                    for i in range(0,int(nvezes)):
                        print(f"Leitura {i+1}: {self.lerDado(int(tipo), int(addr))}") #le o dado de tipo e endereço especificado
                        sleep(self._scan_time)
                elif sel =='2':
                    tipo = input ("""Qual tipo de dado deseja escrever? (1- Holding Register) |2- Coil) :""") #pega tipo de dado a escrever
                    addr = input (f"Digite o endereço da tabela MODBUS: ") #endereço onde deseja escrever
                    valor = input (f"Digite o valor que deseja escrever: ") #valor que deseja escrever
                    self.escreveDado(int(tipo),int(addr),int(valor)) #escreve o dado

                elif sel=='3':
                    scant = input("Digite o tempo de varredura desejado [s]: ")
                    self._scan_time = float(scant) #muda o tempo de escaneamento

                elif sel =='4':
                    self._cliente.close()
                    atendimento = False
                else:
                    print("Seleção inválida")
        except Exception as e:
            print('Erro no atendimento: ',e.args)

    def lerDado(self, tipo, addr):
        """
        Método para leitura de um dado da Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.read_holding_registers(addr,1)[0]

        if tipo == 2:
            return self._cliente.read_coils(addr,1)[0]

        if tipo == 3:
            return self._cliente.read_input_registers(addr,1)[0]

        if tipo == 4:
            return self._cliente.read_discrete_inputs(addr,1)[0]

    def escreveDado(self, tipo, addr, valor):
        """
        Método para a escrita de dados na Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.write_single_register(addr,valor)

        if tipo == 2:
            return self._cliente.write_single_coil(addr,valor)