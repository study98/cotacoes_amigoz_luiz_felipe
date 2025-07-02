import asyncio
from cotacoes.core.dominio.modelo import CotacaoModelo
from datetime import datetime
from zoneinfo import ZoneInfo
from cotacoes.core.services.cotacao_moedas import get_cotacao_dolar, get_cotacao_euro
from cotacoes.core.utils.async_tools import executar_com_seguranca

async def calcular_melhor_cotacao()-> CotacaoModelo:

    resultado_dolar, resultado_euro = await asyncio.gather(
        executar_com_seguranca(lambda: asyncio.to_thread(get_cotacao_dolar)),
        executar_com_seguranca(get_cotacao_euro)
    )
    cotacoes = [
        resultado for resultado in [resultado_dolar, resultado_euro]
        if isinstance(resultado, CotacaoModelo)
    ]
    if not cotacoes:
        raise RuntimeError("Nenhuma cotação válida foi retornada.")
    if len(cotacoes)==1:
        return cotacoes[0]

    return min(cotacoes, key=lambda cotacao: cotacao.valor_cotacao)
