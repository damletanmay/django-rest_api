from rest_framework import serializers
from .models import Advisor,Booking
from django.contrib.auth.models import User

''' these are from docs fo django rest framework which converts our data to JSON format
 also used for making database objects i.e. storing data in database. '''

# for Advisor Model
class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('__all__')

# for user Model
class userRegisterSerilazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')

# for booking Model
class bookingSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('__all__')
