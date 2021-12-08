from django.db.models import fields
from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email  = serializers.CharField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
    
    def validate(self, attrs):
        username_exist = User.objects.filter(username=attrs['username']).exists()

        if username_exist:
            raise serializers.ValidationError(detail='User with username exist')
        
        email_exist = User.objects.filter(username=attrs['email']).exists()

        if email_exist:
            raise serializers.ValidationError(detail='User with username exist')
        
        phone_number_exist = User.objects.filter(username=attrs['phone_number']).exists()

        if phone_number_exist:
            raise serializers.ValidationError(detail='User with phone number exist')

        return super().validate(attrs)

    def create(self, validate_data):
        user = User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            phone_number = validate_data['phone_number']
        )

        user.set_password(validate_data['password'])

        user.save()

        return user