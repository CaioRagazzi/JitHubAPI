from rest_framework.viewsets import ModelViewSet
from perguntas.models import Pergunta
from .serializers import PerguntaSerializer


class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer
