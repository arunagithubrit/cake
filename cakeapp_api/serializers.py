from rest_framework import serializers
from cakeapp.models import User,Cakes,CakeVarients,Carts,Orders,Reviews,Offers


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]

    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class OfferSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    price=serializers.CharField(read_only=True)
    start_date=serializers.CharField(read_only=True)
    due_date=serializers.CharField(read_only=True)
    class Meta:
        model=Offers
        exclude=("cakevarient",)

class CakeVarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    offers=OfferSerializer(many=True,read_only=True)

    class Meta:
        model=CakeVarients
        exclude=('cake',)  

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"



class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    Category=serializers.StringRelatedField(read_only=True)
    varients=CakeVarientSerializer(many=True,read_only=True)
    reviews=ReviewSerializer(many=True,read_only=True)
    avg_rating=serializers.CharField(read_only=True)

    
    class Meta:
        model=Cakes
        fields='__all__'

class CartSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cakevarient=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields=["id","cakevarient","user","status","date"]

class OrderSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    cakevarients=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    ordered_date=serializers.CharField(read_only=True)
    expected_date=serializers.CharField(read_only=True)

    class Meta:
        model=Orders
        fields=["id","user","cakevarients","status","ordered_date","expected_date","address"]

