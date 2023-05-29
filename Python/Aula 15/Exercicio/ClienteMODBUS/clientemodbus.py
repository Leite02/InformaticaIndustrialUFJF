from pyModbusTCP.client import ModbusClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
from time import sleep


class ClienteMODBUS:
    """
    Classe Cliente MODBUS
    """

    def __init__(self, server_ip, porta, scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(
            host=server_ip, port=porta
        )  # cria objeto cliente modbus com ip e porta determinados
        self._scan_time = scan_time  # seta periodo em que "pergunta" para coletar dados

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        self._cliente.open()  # faz a conexão com o servidor
        try:
            atendimento = True  # tipo atendimento do banco
            while atendimento:
                sel = input(
                    "Deseja realizar uma leitura, escrita ou configuração? (1- Leitura | 2- Escrita | 3- Configuração |4- Sair): "
                )
                if sel == "1":
                    tipo = input(
                        """Qual tipo de dado deseja ler? (1- Holding Register |2- Coil |3- Input Register |4- Discrete Input| 5 - Float | 6- Múltiplos bits) :"""
                    )  # pega o tipo de dado a ler
                    addr = input(
                        f"Digite o endereço da tabela MODBUS: "
                    )  # pega o endereço de leitura
                    nvezes = input(
                        "Digite o número de vezes que deseja ler: "
                    )  # pega o nvezes que quer ler
                    for i in range(0, int(nvezes)):
                        print(
                            f"Leitura {i+1}: {self.lerDado(int(tipo), int(addr))}"
                        )  # le o dado de tipo e endereço especificado
                        sleep(self._scan_time)
                elif sel == "2":
                    tipo = input(
                        """Qual tipo de dado deseja escrever? (1- Holding Register) |2- Coil | 3- Float | 4 - Múltiplos Bits) :"""
                    )  # pega tipo de dado a escrever
                    addr = input(
                        f"Digite o endereço da tabela MODBUS: "
                    )  # endereço onde deseja escrever
                    valor = input(
                        f"Digite o valor que deseja escrever: "
                    )  # valor que deseja escrever
                    self.escreveDado(int(tipo), int(addr), valor)  # escreve o dado

                elif sel == "3":
                    scant = input("Digite o tempo de varredura desejado [s]: ")
                    self._scan_time = float(scant)  # muda o tempo de escaneamento

                elif sel == "4":
                    self._cliente.close()
                    atendimento = False
                else:
                    print("Seleção inválida")
        except Exception as e:
            print("Erro no atendimento: ", e.args)

    def lerDado(self, tipo, addr):
        """
        Método para leitura de um dado da Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.read_holding_registers(addr, 1)[0]

        if tipo == 2:
            return self._cliente.read_coils(addr, 1)[0]

        if tipo == 3:
            return self._cliente.read_input_registers(addr, 1)[0]

        if tipo == 4:
            return self._cliente.read_discrete_inputs(addr, 1)[0]

        if tipo == 5:
            leitura = self._cliente.read_holding_registers(addr, 2)
            decoder = BinaryPayloadDecoder.fromRegisters(
                leitura, byteorder=Endian.Big, wordorder=Endian.Big
            )
            return decoder.decode_32bit_float()

        if tipo == 6:
            leitura = self._cliente.read_holding_registers(addr, 1)[0]
            lista_bits = [int(x) for x in "{0:016b}".format(leitura)]
            return lista_bits

    def escreveDado(self, tipo, addr, valor):
        """
        Método para a escrita de dados na Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.write_single_register(addr, int(valor))

        if tipo == 2:
            return self._cliente.write_single_coil(addr, int(valor))

        if tipo == 3:
            builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Big)
            builder.add_32bit_float(float(valor))
            payload = builder.to_registers()
            return self._cliente.write_multiple_registers(addr, payload)

        if tipo == 4:
            posicao = input("Qual posição você deseja alterar? ")
            registrador_lista = list(self.lerDado(6, addr))
            registrador_lista[int(posicao) - 1] = int(valor)
            num = 0
            for i in range(len(registrador_lista)):
                num += registrador_lista[i] * 2**i
            # print(type(registrador_lista[0]))
            # registrador_bin = bin(registrador_lista)
            return self._cliente.write_single_register(addr, num)
