from urllib import response
from django.shortcuts import render , HttpResponse
from users.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.serializers import UserSerializer
from rest_framework import status


@api_view(['POST'])
def addUser(request) :
    user = UserSerializer(data = request.data)
    if user.is_valid():
        user.save()
        return Response(user.errors , status = status.HTTP_201_CREATED)
    return Response(user.errors, status.HTTP_204_NO_CONTENT)
    
@api_view(['DELETE'])
def deleteuser(request , id):
    user = User.objects.get(get = id )
    user.delete()
    result = {
        'status' : "Delete Successful"
    }
    return Response(result, status= status.HTTP_200_OK)


@api_view(['GET'])
def getById(request, id) :
    user = User.objects.get(pk = id)
    serializers = UserSerializer(user)
    return Response(serializers.data)

@api_view(['POST'])
def authApi(request):
    try:
        user = User.objects.get(username= request.data['username'], password= request.data['password'])
        serializer = UserSerializer(user)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except User.DoesNotExist:
        result = {
            "result" : "does not exist"
        }
        return Response(result, status= status.HTTP_401_UNAUTHORIZED)

