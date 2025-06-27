import httpx
from datetime import datetime
from django.conf import settings
from core.dominio.modelo import CotacaoModelo

def get_cotacao_dolar() -> CotacaoModelo:
    url = f"{settings.API_COTACAO}/cotacao/dolar"

    try:
        response = httpx.get(url, timeout=2.0)
        response.raise_for_status()

        data = response.json()

        return CotacaoModelo(
            moeda_melhor_cotacao=data["moeda"],
            sigla_moeda=data["sigla"],
            valor_cotacao=float(data["valor"]),
            momento_cotacao=datetime.fromisoformat(data["momento_cotacao"])
        )

    except (httpx.RequestError, httpx.HTTPStatusError, KeyError, ValueError) as e:
        raise RuntimeError(f"Erro ao consultar cotação do Dolar: {e}")

async def get_cotacao_euro() -> CotacaoModelo:
    url = f"{settings.API_COTACAO}/cotacao/euro"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=6.0)
            response.raise_for_status()

            data = response.json()

            return CotacaoModelo(
                moeda_melhor_cotacao=data["moeda"],
                sigla_moeda=data["sigla"],
                valor_cotacao=float(data["valor"]),
                momento_cotacao=datetime.fromisoformat(data["momento_cotacao"])
            )
    except (httpx.RequestError, httpx.HTTPStatusError, KeyError, ValueError) as e:
        raise RuntimeError(f"Erro ao consultar cotação do Euro: {e}")