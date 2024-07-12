from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import strategiesList
from .serializers import strategyListSerializer
from django.shortcuts import get_object_or_404

@api_view()
def strategies(request):
    scripts = strategiesList.objects.all()
    serialized_script = strategyListSerializer(scripts, many=True)
    return Response(serialized_script.data)

# Serializer for single strategy, get_object_or_404 if does not exist
@api_view()
def single_strategy(request, id):
    scripts = get_object_or_404(strategiesList, pk=id)
    serialized_script = strategyListSerializer(scripts)
    return Response(serialized_script.data)