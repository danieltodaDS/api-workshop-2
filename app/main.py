from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos


# Instancia o objeto da classe principal do framework
app = FastAPI()

# Instancia objeto da lista de produtos
lista_de_produtos = Produtos()


# Cria a rota principal - homepage
@app.get("/") # Request
def hello_world(): # Response
    return {"ola":"mundo"}

# Printa na tela a lista de produtos
@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
    return lista_de_produtos.retorna_lista_produtos()


# Busca produto especifico 
@app.get("/produtos/{id}", response_model=ProdutosSchema)
def busca_produto(id:int):
    return lista_de_produtos.busca_produto(id)


@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema): 
    return lista_de_produtos.adicionar_produtos(produto.model_dump())