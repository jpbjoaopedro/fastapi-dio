from src.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description= 'Nome do centro de treinamento', example='BodyTech', max_length=20)]
    endereco: Annotated[str, Field(description= 'Nome da rua do centro de treinamento', example='Rua Sei lá', max_length=60)]
    proprietario: Annotated[str, Field(description= 'Nome do proprietário do centro de treinamento', example='João', max_length=30)]