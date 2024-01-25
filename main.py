from fastapi import FastAPI

# Instancia o objeto da classe principal do framework
app = FastAPI()

# Cria a rota principal - homepage
@app.get("/") # Request
def hello_world(): # Response
    return {"ola":"mundo"}