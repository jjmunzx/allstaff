from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import NameSerializer
from base.models import Name

@api_view(['GET'])
def show(request):
	db = Name.objects.all()
	serializers = NameSerializer(db,many=True)
	return Response(serializers.data)

@api_view(['GET'])
def getOne(request,pk):
	db = Name.objects.get(id=pk)
	serializers = NameSerializer(db,many=False)
	return Response(serializers.data)

@api_view(['POST'])
def posts(request):
	serializers = NameSerializer(data=request.data)
	if serializers.is_valid():
		serializers.save()
	return Response(serializers.data)

@api_view(['POST'])
def getUpdate(request,pk):
	task = Name.objects.get(id=pk)
	serializers = NameSerializer(instance=task,data = request.data)
	if serializers.is_valid():
		serializers.save()
	return Response(serializers.data)


@api_view(["DELETE"])
def delete(request,pk):
	item = Name.objects.get(id=pk)
	item.delete()
	return Response("ITEM DELETED SUCCESSFULL!")