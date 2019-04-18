from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from formularios.models import Formulario
from perguntas.models import Pergunta
from perguntas.api.serializers import PerguntaSerializer


class FormularioSerializer(ModelSerializer):
    perguntas = PrimaryKeyRelatedField(many=True, queryset=Pergunta.objects.all())

    class Meta:
        model = Formulario
        fields = ('id', 'nome', 'descricao', 'perguntas')

