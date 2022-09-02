from classes.Pedido import Pedido

class Pagamento:
    def __init__(self, pedido: Pedido):
        self.pedido = pedido
        self.pagamento_aprovado = False

    def processa_pagamento(self):
        self.pagamento_aprovado = True
        self.pedido.status = Pedido.PAGO

    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado(self):
        return self.pagamento_aprovado
