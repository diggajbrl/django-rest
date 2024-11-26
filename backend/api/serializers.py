from rest_framework import serializers
from .models import Student

class StudentSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Student
        fields = '__all__'

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be 18 or older.")
        return value