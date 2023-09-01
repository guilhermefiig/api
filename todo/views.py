from rest_framework import viewsets
from todo.models import TodoList, Pessoa
from .serializers import TodoListSerializer, PessoaSerializer

class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer