import httpx
from datetime import datetime
from django.conf import settings
from cotacoes.core.dominio.modelo import CotacaoModelo

def get_cotacao_dolar() -> CotacaoModelo:
    url = f"{settings.API_COTACAO}/cotacao/dolar"

    try:
        response = httpx.get(url, timeout=2.0)
        response.raise_for_status()

        data = response.json()

        return CotacaoModelo(
            moeda_melhor_cotacao=data["currency_name"],
            sigla_moeda=data["currency_kind"],
            valor_cotacao=float(data["currency_price"]/100),
        )

    except (httpx.RequestError, httpx.HTTPStatusError, KeyError, ValueError) as e:
        raise RuntimeError(f"Erro ao consultar cotação do Dolar: {e}")

async def get_cotacao_euro() -> CotacaoModelo:
    url = f"{settings.API_COTACAO}/cotacao/euro"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=4.3)
            response.raise_for_status()

            data = response.json()

            return CotacaoModelo(
                moeda_melhor_cotacao=data["cotacao"]['moeda'],
                sigla_moeda=data["cotacao"]["sigla"],
                valor_cotacao=float(data["cotacao"]["valor_comercial"]),
            )
    except (httpx.RequestError, httpx.HTTPStatusError, KeyError, ValueError) as e:
        raise RuntimeError(f"Erro ao consultar cotação do Euro: {e}")