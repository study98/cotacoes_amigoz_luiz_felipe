from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from core.serializers import CotacaoSerializer
from core.aplicacao.calcular_melhor_cotacao import calcular_melhor_cotacao

class MelhorCotacaoView(APIView):
    @extend_schema(
        summary="Retorna a moeda com melhor cotação",
        description="Compara as cotações disponíveis e retorna a moeda mais barata no momento - Moedas Comparadas Dolar e Euro.",
        responses={200: CotacaoSerializer}
    )
    def get(self, request):
        cotacao = calcular_melhor_cotacao()

        return Response({
            "moeda_melhor_cotacao": cotacao.moeda_melhor_cotacao,
            "sigla_moeda": cotacao.sigla_moeda,
            "valor_cotacao": cotacao.valor_cotacao,
            "momento_cotacao": cotacao.momento_cotacao.isoformat()
        })
