from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import action

from cakeapp_api.serializers import UserSerializer,CakeSerializer
from cakeapp.models import Cakes,CakeVarients
# Create your views here.


class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class CakesView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CakeSerializer
    queryset=Cakes.objects.all()
    model=Cakes

    
    @action(methods=["post"],detail=True)
    def cart_add(self,request,*args,**kwargs):
        vid=kwargs.get("pk")
        varient_obj=CakeVarients.objects.get(id=vid)
        user=request.user
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(clothvarient=varient_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
