from typing import List, Dict

class Produtos: 
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

    def retorna_lista_produtos(self):
        return self.produtos
    

    def busca_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status code": 404, "Mensagem": "Produto nao encontrado"}