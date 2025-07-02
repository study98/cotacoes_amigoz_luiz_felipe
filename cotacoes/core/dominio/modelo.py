from dataclasses import dataclass, field
from datetime import datetime
from zoneinfo import ZoneInfo

@dataclass
class CotacaoModelo:
    moeda_melhor_cotacao: str
    sigla_moeda: str
    valor_cotacao: float
    momento_cotacao: datetime = field(
        default_factory=lambda: datetime.now(ZoneInfo("America/Sao_Paulo"))
    )