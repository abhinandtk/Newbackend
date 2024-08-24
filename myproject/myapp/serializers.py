from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password"]
        extra_kwargs={"password":{"write_only":True}}

    def create(self,validated_data):
        user=User(username=validated_data['username'])
        print(validated_data["password"],'----------------')
        user.set_password(validated_data['password'])   
        user.save()
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id","title","content","created_at","author"]
        extra_kwargs={"author":{"read_only":True}}


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'images']
        
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model=Product
        fields=["id","name","price","status","description","brand","category","created_at","image","rating","images"]
  
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=["id","cart_product","user","created_at","quantity","total_price"]
  
  
class ProductCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    total_quantity = serializers.IntegerField()
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

