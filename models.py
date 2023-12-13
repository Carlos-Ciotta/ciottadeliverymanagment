class Entrega:
    def __init__(self, id = None, nome_cliente = None, logradouro= None, telefone= None, bairro= None, status=None):
        self.id = id
        self.nome_cliente = nome_cliente
        self.logradouro = logradouro
        self.telefone = telefone
        self.data = "NULL"
        self.hora = "NULL"
        self.status = status
        self.bairro = bairro