from contas import Conta,ContaPoupanca

class Banco():
    """
    classe Banco
    """

    def __init__(self):
        self.__contas = [
            Conta(1, senha=1234, titular="João", saldoi=500),
            ContaPoupanca(2, senha=4567, taxa=0.003, titular="José", saldoi=800),
            Conta(3, senha=7890, titular="Maria", saldoi=1000),
        ]
        self.__gerentes = [
            Conta(1, senha=0000, titular="Arthur", saldoi=0),
            Conta(2, senha=1111, titular="Gui", saldoi=0),
        ]
        
    def atendimento(self):
        """
        Método para atendimento geral do banco
        """
        atendimento_geral = True
        while atendimento_geral:
            print("Bem vindo ao sistema de atendimento do banco:")
            print(
                "O que você deseja: 1 - Atendimento ao Cliente, 2 - Atendimento ao Gerente, 3 - Sair"
            )
            escolha = int(input())

            match escolha:
                case 1:
                    self.atendimentoCliente()
                case 2:
                    self.atendimentoGerente()
                case 3:
                    atendimento_geral = False

    def buscaConta(self, numeroconta):
        """
        Metodo para encontrar o numero da conta
        """
        for conta in self.__contas:
            if conta.numero == numeroconta:
                return conta.numero
            return None
    
    def atendimentoCliente(self):
        """
        Método para atendimento ao cliente do banco
        """
        atendimento = True
        print("Bem vindo ao sistema de atendimento ao Cliente")
        print("Digite o número da sua conta: ")
        numeroConta = int(input())
        conta_cliente = self.buscaConta(numeroConta)
        
        print(conta_cliente)
        if numeroConta == None or conta_cliente == None:
            print("Conta inválida")
        else:
            print("Digite a sua senha")
            senhain = int(input())
            if conta_cliente.validaSenha(senhain):
                print("Bem vindo(a)", conta_cliente.titular)
                while atendimento:
                    print("Qual operação deseja fazer? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferencia, 5 - Trocar senha, 6 - Sair)")
                    operacao = int(input())
                    match operacao:
                        case 1:
                            print("Digite a quantia que deseja sacar")
                            valor = int(input())
                            conta_cliente.saque(senhain,valor)
                        case 2: 
                            print("Digite o valor de depósito")
                            valor = int(input())
                            conta_cliente.deposito(senhain,valor)
                        case 3:
                            conta_cliente.getSaldo(senhain)
                        case 4:
                            print("Digite o numero da conta de destino")
                            numero = int(input())
                            conta_destino = self.buscaConta(numero)
                            if numero == None or conta_destino == None:
                                print("Conta inválida")
                            else:
                                print("Digite o valor de transferencia")
                                valor = int(input())
                                conta_cliente.transferencia(senhain,valor,conta_destino)
                        case 5:
                            print("Digite a nova senha: ")
                            senhanova = int(input())
                            conta_cliente.setSenha(senhanova)
                        case 6:
                            atendimento = False
            else:
                print("Senha inválida")    

    def atendimentoGerente(self):
        """
        Método para atendimento do gerente
        """
        atendimento = True
        print("Bem vindo Gerente!")
        print("Digite o seu número de funcionário: ")
        numeroGerente = int(input())

        if numeroGerente == None:
            print("Conta inválida")
        else:
            print("Digite a sua senha: ")
            senhaGerente = int(input())
            if self.__gerentes[numeroGerente - 1].validaSenha(senhaGerente):
                print("Olá ", self.__gerentes[numeroGerente - 1].titular)
                while atendimento:
                    print(
                        "Qual operação deseja fazer? (1 - Criar nova Conta, 2 - Remover Conta, 3 - Sair)"
                    )
                    operacao = int(input())
                    match operacao:
                        case 1:
                            self.criaContaNova(senhaGerente)
                        case 2:
                            self.removeConta(senhaGerente)
                        case 3:
                            atendimento = False
            else:
                print("Senha inválida")
    
    def criaContaNova(self, senha):
        numeroAtualdeContas = len(self.__contas)
        print("Entre com os dados da nova conta: ")
        print("Digite o titular: ")
        nomeTitular = input()

        print("Digite o saldo da conta: ")
        saldoConta = float(input())

        print("Digite a senha da conta: ")
        senhaConta = int(input())

        numeroConta = (self.__contas[numeroAtualdeContas - 1].numero) + 1

        self.__contas.append(Conta(numeroConta, nomeTitular, senhaConta, saldoConta))
        print("Conta criada com sucesso! ")
        print("Dados da nova conta: ")
        self.__contas[numeroAtualdeContas].exibeDados(senhaConta)
        print('')

    def removeConta(self, senha):
        print("Entre com o número da conta a ser deletada: ")
        num_contaremovida = int(input())
        index = 0
        for k in self.__contas:
            if k.numero == num_contaremovida:
                break
            index += 1

        self.__contas.pop(index)
        print("Conta", num_contaremovida, "removida com sucesso")
