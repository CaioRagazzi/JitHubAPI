from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuarios
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)
        queryset = Usuarios.objects.all()
        if nome:
            queryset = Usuarios.objects.filter(nome=nome)
        return queryset
