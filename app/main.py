from fastapi import FastAPI
from .schema import ProdutosSchema
# from .data import Produtos
from .routes import router

# Instancia o objeto da classe principal do framework
app = FastAPI()

app.include_routes(router)