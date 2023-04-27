# Objetos imutáveis

# nome (variável)  | objeto

a = 3  # numero é imutavel, não posso mudar, crio nova variavel e excluo a antiga no ambiente de identificador
b = a

print("Valor: ", a)
print("Identificador de a: ", id(a))
print(
    "Identificador de b antes da mudança: ", id(b)
)  # identificadores ("local da var no python") tem q ser iguais aq
b = 4  # crio nova variavel '4' no ambiente de identificadores e associo b ao 4
print(
    "Identificador de b após a mudança: ", id(b)
)  # identificador agora deve ser diferente

a += 3  # crio nova variavel com valor de 'a' antigo +3 e associo novamente ao 'a'

print("Valor: ", a)
print(
    "Identificador: ", id(a)
)  # identificador de a agora será diferente também do anterior

a = "Informática"

# Objetos mutáveis
# nome (variável)  | objeto
a = [1, 2, 3]  # agora a tem uma lista atribuida, que é mutavel
b = a  # atribuimos a b a mesma coisa que está em 'a'
b.append(
    4
)  # alteramos b, como o identificador de b e a são o mesmo, e a lista é mutável, alteramos a var 'a' tbm
print("Valor: ", a)  # verificamos que 'a' mudou de valor
print("Identificador: ", id(a))  # verificamos que ambos tem o mesmo id
print("Identificador: ", id(b))

a.append(5)
print("Valor: ", a)
print("Identificador: ", id(a))
