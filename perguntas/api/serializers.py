from rest_framework.serializers import ModelSerializer
from perguntas.models import Pergunta

class PerguntaSerializer(ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ('id', 'nome', 'descricao', 'tipo')
