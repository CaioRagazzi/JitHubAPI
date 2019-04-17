from rest_framework.viewsets import ModelViewSet
from formularios.models import Formulario
from .serializers import FormularioSerializer


class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
