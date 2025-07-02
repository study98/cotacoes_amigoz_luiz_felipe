import asyncio
from typing import Callable, Awaitable, Union
from cotacoes.core.dominio.modelo import CotacaoModelo
import logging

logger = logging.getLogger(__name__)

async def executar_com_seguranca(chamada: Callable[[], Awaitable]) -> Union[CotacaoModelo, Exception]:
    try:
        resultado = chamada()
        if asyncio.iscoroutine(resultado):
            return await resultado
    except Exception as e:
        logger.warning(f"[AVISO] Erro durante chamada de cotação: {e}")
        return e