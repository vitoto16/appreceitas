from django.shortcuts import render
from receitas.models import Receita

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReceitaSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/lista-receitas/',
        'Detail View': '/detalhe-receita/<str:pk>/',
        'Create': '/cria-receita/',
        'Update': '/atualiza-receita/<str:pk>/',
        'Delete': '/deleta-receita/<str:pk>/',
    }

    return Response(api_urls)

# @api_view(['GET'])
# def listaReceitas(request):
#     receitas = Receita.objects.all().filter(publicada=True)
#     serializer = ReceitaSerializer(receitas, many=True)
#     return Response(serializer.data)

class ListaReceitas(generics.ListAPIView):
    serializer_class = ReceitaSerializer

    def get_queryset(self):
        queryset = Receita.objects.all()
        pessoa = self.request.query_params.get('pessoa')

        if pessoa:
            queryset = queryset.filter(pessoa__username=pessoa)

        return queryset

@api_view(['GET'])
def detalheReceita(request, pk):
    receita = Receita.objects.get(id=pk)
    serializer = ReceitaSerializer(receita, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def criaReceita(request):
    serializer = ReceitaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def atualizaReceita(request, pk):
    receita = Receita.objects.get(id=pk)
    serializer = ReceitaSerializer(instance=receita, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletaReceita(request, pk):
    receita = Receita.objects.get(id=pk)
    receita.delete()

    return Response("Item deletado com sucesso!")