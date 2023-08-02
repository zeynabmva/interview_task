from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["GET" , "POST"])
def user_list_view(request):
    if request.method =="GET":
        obj = User.objects.all()
        serializer = UserSerializer(obj , many=True)

        return Response(serializer.data , )
    

    elif request.method =="POST":
        # data = JSONParser().parse(request)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET" , "PATCH" , "DELETE"])
def user_detail_view(request , id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=404)
    

    if request.method =="GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        # data = JSONParser().parse(request)
        serializer = UserSerializer(user , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =="DELETE":
        user.delete()
        return Response(status=204)

    
     