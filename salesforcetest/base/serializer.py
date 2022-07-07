from rest_framework import serializers
from .models import *


class OppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'

class AccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = '__all__'