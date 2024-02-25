from pydantic import BaseModel, PositiveInt


class ProdutosSchema(BaseModel): 
    id: int
    titulo: str
    descricao: str
    preco: PositiveInt
    