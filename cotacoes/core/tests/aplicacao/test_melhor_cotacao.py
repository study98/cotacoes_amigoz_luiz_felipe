import pytest
from unittest.mock import patch
from cotacoes.core.aplicacao.calcular_melhor_cotacao import calcular_melhor_cotacao
from cotacoes.core.tests.mocks.mock_cotacao_api import (
    mock_get_cotacao_dolar,
    mock_get_cotacao_euro,
    mock_get_cotacao_dolar_erro,
    mock_get_cotacao_euro_erro
)

@pytest.mark.asyncio
@patch("cotacoes.core.aplicacao.calcular_melhor_cotacao.get_cotacao_dolar", new=mock_get_cotacao_dolar)
@patch("cotacoes.core.aplicacao.calcular_melhor_cotacao.get_cotacao_euro", new=mock_get_cotacao_euro)
async def test_retorna_melhor_cotacao():
    resultado = await calcular_melhor_cotacao()

    assert resultado.moeda_melhor_cotacao in ["dollar", "euro"]
    assert 1.0 <= resultado.valor_cotacao <= 10.0 


@pytest.mark.asyncio
@patch("cotacoes.core.aplicacao.calcular_melhor_cotacao.get_cotacao_dolar", new=mock_get_cotacao_dolar_erro)
@patch("cotacoes.core.aplicacao.calcular_melhor_cotacao.get_cotacao_euro", new=mock_get_cotacao_euro_erro)
async def test_erro_se_ambas_falham():

    with pytest.raises(RuntimeError, match="Nenhuma cotação válida foi retornada"):
        await calcular_melhor_cotacao()