from rest_framework import serializers
from .models import Student

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