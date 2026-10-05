"""
PLANO (passo 1) - Ciclo Vermelho-Verde-Refatorar

Problema: fechamento de pedido de uma loja online. Dado o tipo de cliente e a lista
de itens (preco_unitario, quantidade), calcular subtotal, desconto, frete e total.

Casos que serao testados (tres variacoes de comportamento + validacoes):
  1. Cliente "comum":     sem desconto, frete fixo de R$ 20,00.
  2. Cliente "estudante": 15% de desconto sobre o subtotal, frete fixo de R$ 20,00.
  3. Cliente "premium":   10% de desconto sobre o subtotal, frete gratis.
  4. Tipo de cliente desconhecido -> ValueError.
  5. Pedido sem itens -> ValueError.

Padrao de projeto escolhido: Template Method (visto em aula).
Por que: a sequencia do fechamento e igual para todo tipo de cliente
(subtotal -> desconto -> frete -> total); so dois passos variam (desconto e frete).
Na versao "verde" isso fica num if/elif; cada novo tipo de cliente obrigaria a mexer
nessa cadeia e nada protegeria a ordem dos passos. O Template Method deixa a ordem
em um unico lugar e faz cada tipo implementar apenas os dois passos que variam.

Tempo planejado (total 120 min):
  - Plano: 10 min
  - Vermelho (testes + ver falhar + commit red): 15 min
  - Verde (implementacao direta + commit green): 10 min  -> red e green prontos aos 25 min
  - Refatorar (Template Method + commit refactor): 50 min (inclui margem)
  - Autoavaliacao e envio: 10 min
  - Folga: 25 min

Uso de IA: sim. A IA foi usada para propor o problema, escrever os testes, o codigo
nas tres fases e rascunhar a autoavaliacao (detalhes no fim de pedido.py).
"""
import pytest

from pedido import fechar_pedido

ITENS = [(50.0, 2), (30.0, 1)]  # subtotal = 130,00


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
