from rest_framework import serializers
from .models import Login, Register, Profile 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Login
        fields = ['phone_number', 'password']

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password']
        

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password']

        def create(self,validated_data):
            password = validated_data.pop('password')
            validated_data['password'] = make_password(password)
            
             
             #hash the password before creating the user
            user = User.objects.create(**validated_data)
            #create the user profile 

            profile, created = Profile.objects.get_or_create(user=user)
            return user 


        