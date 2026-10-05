"""
Plano da atividade do ciclo Vermelho-Verde-Refatorar.

O problema é fazer o fechamento de um pedido de uma loja.
Tem subtotal, desconto, frete e total.

Os testes são:
1. Cliente comum: sem desconto e frete de 20 reais.
2. Estudante: 15% de desconto e frete de 20 reais.
3. Premium: 10% de desconto e frete gratis.
4. Tipo de cliente errado da erro.
5. Pedido sem itens da erro.

Foi usado Template Method porque a conta é quase igual para todos.
O que muda é o desconto e o frete.

Tempo planejado:
- RED: 25 minutos
- GREEN: 35 minutos
- REFACTOR: 30 minutos
- Teste final e autoavaliacao: 10 minutos

Uso de IA: sim. A IA ajudou a montar os testes e o codigo das fases.
O problema foi na organizacao dos commits. Em vez de deixar cada fase
com seu codigo e seu commit separado, acabou ficando um commit com os
tres updates. Isso deixou o historico diferente do que a atividade pedia.
"""
import pytest

from pedido import fechar_pedido

ITENS = [(50.0, 2), (30.0, 1)]  # da 130 reais


def test_cliente_comum_sem_desconto_e_com_frete_fixo():
    r = fechar_pedido("comum", ITENS)
    assert r.subtotal == pytest.approx(130.0)
    assert r.desconto == pytest.approx(0.0)
    assert r.frete == pytest.approx(20.0)
    assert r.total == pytest.approx(150.0)


def test_cliente_estudante_tem_15_por_cento_de_desconto_e_frete_fixo():
    r = fechar_pedido("estudante", ITENS)
    assert r.subtotal == pytest.approx(130.0)
    assert r.desconto == pytest.approx(19.5)
    assert r.frete == pytest.approx(20.0)
    assert r.total == pytest.approx(130.5)


def test_cliente_premium_tem_10_por_cento_de_desconto_e_frete_gratis():
    r = fechar_pedido("premium", ITENS)
    assert r.subtotal == pytest.approx(130.0)
    assert r.desconto == pytest.approx(13.0)
    assert r.frete == pytest.approx(0.0)
    assert r.total == pytest.approx(117.0)


def test_tipo_de_cliente_desconhecido_levanta_erro():
    with pytest.raises(ValueError):
        fechar_pedido("visitante", ITENS)


def test_pedido_sem_itens_levanta_erro():
    with pytest.raises(ValueError):
        fechar_pedido("comum", [])
