from fastapi import FastAPI
from typing import List, Dict

# Instancia o objeto da classe principal do framework
app = FastAPI()

produtos: List [Dict[str, any]] = [
    {
        "id": 1,
        "nome":"Celular",
        "descricao": "aparelho celular",
        "preco": 2131
    },
    {
        "id": 2,
        "nome":"Monitor",
        "descricao": "monitor 8k",
        "preco": 412
    },
    {
        "id": 3,
        "nome":"Fone de ouvido",
        "descricao": "fone de ouvido auricular",
        "preco": 1212
    }
]

# Cria a rota principal - homepage
@app.get("/") # Request
def hello_world(): # Response
    return {"ola":"mundo"}

# Printa na tela a lista de produtos
@app.get("/produtos")
def retorna_lista_produtos():
    return produtos