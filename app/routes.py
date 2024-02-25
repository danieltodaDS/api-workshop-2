from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schema import ProdutosSchema
from .config import get_db
from .model import Produto

router = APIRouter()


# Cria a rota principal - homepage
@router.get("/") # Request
def hello_world(): # Response
    return {"ola":"mundo"}


# Printa na tela a lista de produtos
@router.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()


# Busca produto especifico 
@router.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def busca_produto(produto_id:int, db:Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")


@router.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema, db: Session = Depends(get_db)): 
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.delete("/produtos/{produto_id}", response_model=ProdutosSchema)
def remover_produto(produto_id:int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else: 
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    

@router.put("/produtos/{produto_id}", response_model = ProdutosSchema)
def atualizar_produto(
    produto_id: int, produto_data:ProdutosSchema, db: Session = Depends(get_db)
):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh(db_produto)
        
        return db_produto
    else: 
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
