from modbuspersistencia import ModbusPersistencia

#dicionário com dados a serem utilizados
tags_addrs = {
    'temperatura': 1000,
    'pressao': 1001,
    'umidade': 1002,
    'consumo': 1003,
}
c = ModbusPersistencia('localhost',502, tags_addrs)
c.run()