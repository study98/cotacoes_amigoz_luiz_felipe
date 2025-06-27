from typing import Callable, Awaitable, Union
from core.dominio.modelo import CotacaoModelo

async def executar_com_seguranca(chamada: Callable[[], Awaitable]) -> Union[CotacaoModelo, Exception]:
    try:
        return await chamada()
    except Exception as e:
        print(f"[AVISO] Erro durante chamada de cotação: {e}")
        return e