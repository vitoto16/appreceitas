from rest_framework import serializers
from receitas.models import Receita

class ReceitaSerializer(serializers.ModelSerializer):
    pessoa = serializers.StringRelatedField()

    class Meta:
        model = Receita
        fields = ['pessoa',
                  'nome_receita',
                  'ingredientes',
                  'modo_de_preparo',
                  'tempo_de_preparo',
                  'rendimento',
                  'categoria',
                  'data_receita',
                  'foto_receita'
                  ]