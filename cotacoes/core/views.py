import time
import asyncio
import logging
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cotacoes.core.serializers import CotacaoSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample
from cotacoes.core.aplicacao.calcular_melhor_cotacao import calcular_melhor_cotacao


logg = logging.getLogger(__name__)

class MelhorCotacaoView(APIView):
    @extend_schema(
        summary="Retorna a moeda com melhor cotação",
        description="Compara as cotações disponíveis e retorna a moeda mais barata no momento - Moedas Comparadas Dolar e Euro.",
        responses={200: CotacaoSerializer},
        examples=[
            OpenApiExample(
                "Exemplo de resposta",
                value={
                    "moeda": "dollar",
                    "sigla": "USD",
                    "valor": 5.73,
                    "momento_cotacao": "2025-06-25T22:35:00-03:00"
                },
                response_only=True
            )
        ]
    )
    def get(self, request):
        logg.info("-> Iniciada a requisição: /api/melhor-cotacao/")
        inicio = time.perf_counter()
        cotacao = asyncio.run(calcular_melhor_cotacao()) 
        fim = time.perf_counter()
        tempo_execucao = fim-inicio
        logg.info(f"-> Melhor Cotação: {cotacao.moeda_melhor_cotacao} - {cotacao.valor_cotacao}")
        logg.info(f"-> Tempo de processamento: {tempo_execucao:.2f} segundos")

        return Response({
            "moeda_melhor_cotacao": cotacao.moeda_melhor_cotacao,
            "sigla_moeda": cotacao.sigla_moeda,
            "valor_cotacao": cotacao.valor_cotacao,
            "momento_cotacao": cotacao.momento_cotacao.isoformat()
        })
