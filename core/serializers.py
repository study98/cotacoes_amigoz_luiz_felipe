from rest_framework import serializers

class CotacaoSerializer(serializers.Serializer):
    moeda_melhor_cotacao = serializers.CharField(help_text="Nome da moeda com melhor cotação (ex: Dolar, Euro)")
    sigla_moeda = serializers.CharField(help_text="Sigla/Código da moeda (ex: USD, EUR)")
    valor_cotacao = serializers.FloatField(help_text="Valor atual da cotação em reais")
    momento_cotacao = serializers.DateTimeField(help_text="Momento da consulta da cotação (formato ISO 8601, GMT-3)")

    class Meta:
        ref_name = "CotacaoResponse"