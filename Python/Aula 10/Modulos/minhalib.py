#Cria funções que podem ser utilizadas em outros codigos
def soma(op1,op2): #Os comentarios Entre """....""" aparecem ao se digitar a função no arquivo .py, 
    #possibilitando outros programadores terem uma breve impressão a utilização da função
    #podedmos optar por fazer (op1:int,op2:int)->int para determinar tipo do op1,op2 e retorno
    # é interessante!! 
    """  
    Função que retorna a soma de dois números
    :param op1: primeiro operando
    :param op2: segundo operando
    :return : soma dos operandos
    """
    return op1+op2

def divisao(dividendo,divisor):
    """
    Função que retorna a divisão do dividendo pelo divisor
    :param dividendo: dividendo da operação
    :param divisor: divisor da operação
    :return : divisão do dividendo pelo divisor
    """
    return dividendo/divisor

lista =  [x**2 for x in range(0,10)]#Cria uma lista desse tipo:[0,1,4,9,16,25,...,100]


#ao colocar essa estrutura, damos ao usuario a opção de utilizar as funcoes direto do terminal
#no terminal: python -m minhalib param1 param2 param3
# uso da sys para pegar dados do terminal
#sysargv[3] é o param3
if __name__ == "__main__":    #Não são executadas quando se o utiliza o import
    import sys
    if sys.argv[3] == "+":
        print(soma(float(sys.argv[1]),float(sys.argv[2]))) 
    elif sys.argv[3] == "/":
        print(divisao(float(sys.argv[1]),float(sys.argv[2])))
    else:
        print("Operação inválida")
