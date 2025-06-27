from dataclasses import dataclass
from datetime import datetime

@dataclass
class CotacaoModelo:
    moeda_melhor_cotacao: str
    sigla_moeda: str
    valor_cotacao: float
    momento_cotacao: datetime