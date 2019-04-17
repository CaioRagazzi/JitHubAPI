from rest_framework.serializers import ModelSerializer
from formularios.models import Formulario

class FormularioSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields = ('id', 'nome', 'descricao', 'pergunta')
