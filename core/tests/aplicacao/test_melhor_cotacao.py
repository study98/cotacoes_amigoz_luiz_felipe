import pytest
from datetime import datetime
from unittest.mock import AsyncMock, patch
from core.dominio.modelo import CotacaoModelo
from core.aplicacao.calcular_melhor_cotacao import calcular_melhor_cotacao

@pytest.mark.asyncio
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_dolar")
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_euro")
async def test_retorna_menor_cotacao(mock_euro, mock_dolar):
    mock_dolar.return_value = CotacaoModelo("Dolar", "USD", 5.60, datetime.now())
    mock_euro.return_value = CotacaoModelo("Euro", "EUR", 5.45, datetime.now())

    resultado = await calcular_melhor_cotacao()

    assert resultado.moeda_melhor_cotacao == "Euro"
    assert resultado.valor_cotacao == 5.45

@pytest.mark.asyncio
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_dolar")
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_euro")
async def test_falha_cotacao_dolar(mock_euro, mock_dolar):
    mock_dolar.return_value = RuntimeError("Falha na cotação do Dolar")
    mock_euro.return_value = CotacaoModelo("Euro", "EUR", 5.50, datetime.now())

    resultado = await calcular_melhor_cotacao()

    assert resultado.moeda_melhor_cotacao == "Euro"

@pytest.mark.asyncio
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_dolar")
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_euro")
async def test_falha_cotacao_euro(mock_euro, mock_dolar):
    mock_dolar.return_value = CotacaoModelo("Dolar", "USD", 5.50, datetime.now())
    mock_euro.return_value = RuntimeError("Falha na cotação do Euro")

    resultado = await calcular_melhor_cotacao()

    assert resultado.moeda_melhor_cotacao == "Dolar"

@pytest.mark.asyncio
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_dolar")
@patch("core.aplicacao.calcular_melhor_cotacao.get_cotacao_euro")
async def test_erro_se_ambas_falham(mock_euro, mock_dolar):
    mock_dolar.return_value = RuntimeError("Falha no dólar")
    mock_euro.return_value = RuntimeError("Falha no euro")

    with pytest.raises(RuntimeError, match="Nenhuma cotação válida foi retornada"):
        await calcular_melhor_cotacao()