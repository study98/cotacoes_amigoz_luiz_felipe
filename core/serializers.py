from rest_framework import serializers

class CotacaoSerializer(serializers.Serializer):
    moeda_melhor_cotacao = serializers.CharField()
    sigla_moeda = serializers.CharField()
    valor_cotacao = serializers.FloatField()
    momento_cotacao = serializers.DateTimeField()