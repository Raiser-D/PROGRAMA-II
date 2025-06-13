from config import *
from pony.orm import Required, Optional
from datetime import date, datetime
from config import db 

class Pessoa(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)
    cpf = Required(str)
    rg = Required(str)
    dt_nasc = Required(date, default=date(2000, 1, 1))
    cep = Required(str)
    rua = Optional(str)
    bairro = Optional(str)
    num_casa = Required(int)
    peso = Required(float)

    def __str__(self):
        return (
            f'ID: {self.id}, '
            f'Nome: {self.nome}, '
            f'Email: {self.email}, '
            f'Telefone: {self.telefone or "sem telefone"}, '
            f'CPF: {self.cpf}, '
            f'RG: {self.rg}, '
            f'Data de Nascimento: {self.dt_nasc}, '
            f'CEP: {self.cep}, '
            f'Rua: {self.rua or "não informado"}, '
            f'Bairro: {self.bairro or "não informado"}, '
            f'Número da Casa: {self.num_casa}'
            f'Peso: {self.peso}'
        )
        
        
db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)
