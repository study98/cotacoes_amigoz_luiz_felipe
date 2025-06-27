from core.dominio.modelo import CotacaoModelo
from datetime import datetime
from zoneinfo import ZoneInfo

def calcular_melhor_cotacao():
    # Resposta base
    data_hora = datetime.now(tz=ZoneInfo("America/Sao_Paulo"))

    return CotacaoModelo(
        moeda_melhor_cotacao="Dolar",
        sigla_moeda="USD",
        valor_cotacao=5.80,
        momento_cotacao=data_hora
    )
