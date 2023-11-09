from rest_framework import serializers
from cakeapp.models import User,Cakes,CakeVarients


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]

    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CakeVarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=CakeVarients
        exclude=('cake',)  

class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    Category=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Cakes
        fields='__all__'

