from rest_framework import serializers
from .models import CelebrityTable

class CelebritySerializer(serializers.ModelSerializer):

    class Meta:
        model = CelebrityTable
        fields = '__all__'