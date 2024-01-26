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
@app.get("/produtos")
def listar_produtos():
    return lista_de_produtos.retorna_lista_produtos()


# Busca produto especifico 
@app.get("/produtos/{id}")
def busca_produto(id:int):
    return lista_de_produtos.busca_produto()

    # for produto in produtos:
    #     if produto["id"] == id:
    #         return produto
    # return {"Status code": 404, "Mensagem": "Produto nao encontrado"}

