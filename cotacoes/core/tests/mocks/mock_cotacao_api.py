import random
import time
from cotacoes.core.dominio.modelo import CotacaoModelo

def mock_get_cotacao_dolar() -> CotacaoModelo:
    valor = round(random.uniform(1.0, 10.0), 2)
    return CotacaoModelo(
        moeda_melhor_cotacao="dollar",
        sigla_moeda="USD",
        valor_cotacao=valor,
    )

def mock_get_cotacao_euro() -> CotacaoModelo:
    delay = round(random.uniform(0.9, 4.8), 2)
    time.sleep(delay)  # Simula latência real
    valor = round(random.uniform(1.0, 10.0), 2)
    return CotacaoModelo(
        moeda_melhor_cotacao="euro",
        sigla_moeda="EUR",
        valor_cotacao=valor,
    )

def mock_get_cotacao_dolar_erro():
    raise RuntimeError("Falha na cotação do Dolar")

def mock_get_cotacao_euro_erro():
    raise RuntimeError("Falha na cotação do Euro")