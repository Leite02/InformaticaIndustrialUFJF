from contas import Conta, ContaPoupanca


class Banco:
    """
    Classe Banco
    """

    def __init__(self):
        self.__contas = [
            Conta(1, senha=1234, titular="João", saldoi=500),
            ContaPoupanca(2, senha=4567, taxa=0.003, titular="José", saldoi=800),
            Conta(3, senha=7890, titular="Maria", saldoi=1000),
        ]
        self.__gerentes = [
            Conta(1, senha=6655, titular="Bernardo", saldoi=-100),
            Conta(2, senha=4455, titular="Moyses", saldoi=-100),
        ]

    def atendimento(self):
        """
        Método para atendimento geral do banco
        """
        status_atendimento = True
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
                    status_atendimento = False
                    atendimento_geral = False

    def atendimentoCliente(self):
        """
        Método para atendimento ao cliente do banco
        """
        atendimento = True
        print("Bem vindo ao sistema de atendimento ao Cliente")
        print("Digite o número da sua conta: ")
        numeroConta = int(input())

        if numeroConta == None:
            print("Conta inválida")
        else:
            print("Digite a sua senha: ")
            senhain = int(input())
            if self.__contas[numeroConta - 1].validaSenha(senhain):
                print("Olá ", self.__contas[numeroConta - 1].titular)
                while atendimento:
                    print(
                        "Qual operação deseja fazer? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Trocar senha, 5 - Sair)"
                    )
                    operacao = int(input())
                    match operacao:
                        case 1:
                            print("Digite o valor: ")
                            valor = float(input())
                            self.__contas[numeroConta - 1].saque(senhain, valor)
                        case 2:
                            print("Digite o valor: ")
                            valor = float(input())
                            self.__contas[numeroConta - 1].deposito(valor)
                        case 3:
                            self.__contas[numeroConta - 1].exibeDados(senhain)
                        case 4:
                            print("Digite a nova senha: ")
                            senhanova = int(input())
                            self.__contas[numeroConta - 1].setSenha(senhanova)
                        case 5:
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
                        "Qual operação deseja fazer? (1 - Criar nova Conta, 2 - Sair)"
                    )
                    operacao = int(input())
                    match operacao:
                        case 1:
                            self.criaContaNova(senhaGerente)
                        case 2:
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

        numeroConta = numeroAtualdeContas + 1

        self.__contas.append(Conta(numeroConta, nomeTitular, senhaConta, saldoConta))
        print("Conta criada com sucesso! ")
        print("Dados da nova conta: ")
        self.__contas[numeroAtualdeContas].exibeDados(senhaConta)
