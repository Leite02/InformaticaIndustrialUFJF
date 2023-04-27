param1 = {
    "Descrição": "Acesso aos Parâmetros",
    "Faixa de valores": "0 a 9999",
    "Ajuste de Fábrica": 0,
    "Ajuste do usuário": None,
    "Propr.": None,
    "Grupos": None,
    "Pág.": "5-2",
}
param2 = {
    "Descrição": "Referência velocidade",
    "Faixa de valores": "0 a 65535",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-1",
}
param3 = {
    "Descrição": "Velocidade de saída (Motor)",
    "Faixa de valores": "0 a 65535",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-1",
}
param4 = {
    "Descrição": "Corrente do Motor",
    "Faixa de valores": "0,0 a 200,0 A",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-1",
}
param5 = {
    "Descrição": "Acesso aos Parâmetros",
    "Faixa de valores": "0 a 9999",
    "Ajuste de Fábrica": 0,
    "Ajuste do usuário": None,
    "Propr.": None,
    "Grupos": None,
    "Pág.": "5-2",
}
param6 = {
    "Descrição": "Tensão Barram. CC (Ud)",
    "Faixa de valores": "0 a 2000V",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-1",
}
param7 = {
    "Descrição": "Frequência de Saída (Motor)",
    "Faixa de valores": "0,0 a 500,0 Hz",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-2",
}

param8 = {
    "Descrição": "Estado do Inversor",
    "Faixa de valores": "0 = Ready(Pronto) \n 1 = Run (Execução) \n 2 = Subtensão \n 3 = Falha \n 4 = Autoajuste \n 5 = Configuração \n 6 = Frenagem CC \n 7 = Estado Dormir",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-2",
}

param9 = {
    "Descrição": "Tensão de Saída",
    "Faixa de valores": "0 a 2000V",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-3",
}

param10 = {
    "Descrição": "Torque no Motor",
    "Faixa de valores": "-1000,0 a 1000,0%",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-3",
}

param11 = {
    "Descrição": "Potência de Saída",
    "Faixa de valores": "0,0 a 6553,5 kW",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-4",
}

param12 = {
    "Descrição": "Fator de Potência",
    "Faixa de valores": "-1,00 a 1,00",
    "Ajuste de Fábrica": None,
    "Ajuste do usuário": None,
    "Propr.": "ro",
    "Grupos": "READ",
    "Pág.": "17-4",
}

dicionarioInversor = {
    "P0000": param1,
    "P0001": param2,
    "P0002": param3,
    "P0003": param4,
    "P0004": param5,
    "P0005": param6,
    "P0006": param7,
    "P0007": param8,
    "P0008": param9,
    "P0009": param10,
    "P0010": param11,
    "P0011": param12,
}

for key, value in dicionarioInversor.items():
    print(key, "->", value)
