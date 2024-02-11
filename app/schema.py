from pydantic import BaseModel, PositiveInt


class ProdutosSchema(BaseModel): 
    id: int
    nome: str
    descricao: str
    preco: PositiveInt
    