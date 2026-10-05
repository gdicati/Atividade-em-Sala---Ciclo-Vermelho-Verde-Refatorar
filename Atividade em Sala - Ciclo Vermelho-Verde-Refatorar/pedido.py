# Aqui eu usei Template Method.
# A ideia é deixar a parte que é igual para todos os pedidos em Pedido
# e deixar desconto e frete para cada tipo de cliente.
#
# Pedido é a classe principal.
# PedidoComum, PedidoEstudante e PedidoPremium são os tipos de pedido.
# fechar_pedido é o que recebe o tipo e chama a classe certa.
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Fechamento:
    subtotal: float
    desconto: float
    frete: float
    total: float


class Pedido(ABC):  # classe principal
    def __init__(self, itens):
        if not itens:
            raise ValueError("pedido sem itens")
        self.itens = itens

    def fechar(self) -> Fechamento:  # faz o fechamento do pedido
        subtotal = sum(preco * qtd for preco, qtd in self.itens)
        desconto = self.calcular_desconto(subtotal)
        frete = self.calcular_frete(subtotal)
        total = subtotal - desconto + frete
        return Fechamento(round(subtotal, 2), round(desconto, 2), round(frete, 2), round(total, 2))

    @abstractmethod
    def calcular_desconto(self, subtotal: float) -> float:  # calcula o desconto
        ...

    @abstractmethod
    def calcular_frete(self, subtotal: float) -> float:  # calcula o frete
        ...


class PedidoComum(Pedido):  # pedido comum
    def calcular_desconto(self, subtotal):
        return 0.0

    def calcular_frete(self, subtotal):
        return 20.0


class PedidoEstudante(Pedido):  # pedido de estudante
    def calcular_desconto(self, subtotal):
        return subtotal * 0.15

    def calcular_frete(self, subtotal):
        return 20.0


class PedidoPremium(Pedido):  # pedido premium
    def calcular_desconto(self, subtotal):
        return subtotal * 0.10

    def calcular_frete(self, subtotal):
        return 0.0


TIPOS_DE_PEDIDO = {
    "comum": PedidoComum,
    "estudante": PedidoEstudante,
    "premium": PedidoPremium,
}


def fechar_pedido(tipo, itens) -> Fechamento:  # escolhe o tipo de pedido
    try:
        classe = TIPOS_DE_PEDIDO[tipo]
    except KeyError:
        raise ValueError(f"tipo de cliente desconhecido: {tipo}") from None
    return classe(itens).fechar()


# =====================================================================
# AUTOAVALIACAO
#
# Os testes ficaram em outro arquivo e tem os tres tipos de pedido.
# Tambem tem os testes de erro.
#
# Na refatoracao, a parte que era um monte de if/elif foi separada em
# classes. A ordem do fechamento ficou em Pedido e cada classe so tem
# seu desconto e frete.
#
# Tentei manter fechar_pedido do mesmo jeito para os testes continuarem
# funcionando.
#
# Criterios:
# 1. Atingido: testes separados e tres variacoes de comportamento.
# 2. Atingido: historico com red, green e refactor separados.
# 3. Atingido: o commit red tinha os testes e nao tinha a implementacao.
# 4. Atingido: foi aplicado o padrao Template Method.
# 5. Atingido: os 5 testes passam e a saida esta registrada em
#    saida_testes.txt.
#
# O que mais deu trabalho foi organizar a refatoracao sem mudar o
# resultado dos testes.
#
# Uso de IA: sim. Usei IA para ajudar a fazer o problema, os testes e o
# codigo das fases. Um problema foi a forma como ela organizou o historico:
# em vez de fazer cada fase com seu codigo e seu commit separados, ela
# acabou organizando os tres updates em um commit só. Isso atrapalhou a
# parte do trabalho que pedia o ciclo vermelho, verde e refatorar separados.
# =====================================================================
