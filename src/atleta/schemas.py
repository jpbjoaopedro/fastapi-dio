from typing import Annotated
from pydantic import Field, PositiveFloat
from src.contrib.schemas import BaseSchema

class Atleta (BaseSchema):
    nome: Annotated[str, Field(description= 'Nome do atleta', examples='Joao', max_length=50)]
    cpf: Annotated[str, Field(description= 'CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int, Field(description= 'Idade do atleta', examples='22', max_digits=2)]
    peso: Annotated[PositiveFloat, Field(description= 'Peso do atleta', examples='78.2')]
    altura: Annotated[PositiveFloat, Field(description= 'Altura do atleta', examples='1.77')]
    sexo: Annotated[str, Field(description= 'Sexo do atleta', examples='M', max_length=1)]