from rest_framework import serializers
from .models import Student, Category, Book
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
 
    def validate(self, data):
        if 'name' in data and data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError("Name cannot contain digits")

        if 'age' in data and data['age']:
            if data['age'] < 18:
                raise serializers.ValidationError("Age cannot be less than 18")
        
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name',]

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = "__all__"
        #depth = 1