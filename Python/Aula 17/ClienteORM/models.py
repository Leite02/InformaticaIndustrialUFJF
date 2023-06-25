from db import Base
from sqlalchemy import Column, Integer, DateTime

#Implementa a classe DadoCLP a partir da Base do sqlalchemy
class DadoCLP(Base):
    """
    Modelo dos dados do CLP
    """
    #como não temos construtor, usa o da base
    __tablename__ = 'dadoclp' #nome da tabela
    id = Column(Integer, primary_key=True) #id principal
    timestamp = Column(DateTime) #coluna timestamp
    temperatura = Column(Integer) #coluna temperatura, etc...
    pressao = Column(Integer)
    umidade = Column(Integer)
    consumo = Column(Integer)

    def get_attr_printable_list(self): #método auxiliar p/ ajudar a printar os dados na tela
        return [self.id,
        self.timestamp.strftime('%d/%m/%Y %H:%M:%S'),
        self.temperatura,
        self.pressao,
        self.umidade,
        self.consumo]
