from dataclasses import dataclass


@dataclass(frozen=True)
class Fechamento:
    subtotal: float
    desconto: float
    frete: float
    total: float


def fechar_pedido(tipo, itens):
    if not itens:
        raise ValueError("pedido sem itens")

    subtotal = sum(preco * qtd for preco, qtd in itens)

    if tipo == "comum":
        desconto = 0.0
        frete = 20.0
    elif tipo == "estudante":
        desconto = subtotal * 0.15
        frete = 20.0
    elif tipo == "premium":
        desconto = subtotal * 0.10
        frete = 0.0
    else:
        raise ValueError(f"tipo de cliente desconhecido: {tipo}")

    total = subtotal - desconto + frete
    return Fechamento(round(subtotal, 2), round(desconto, 2), round(frete, 2), round(total, 2))
