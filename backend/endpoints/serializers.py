from rest_framework import serializers
from .models import *

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model=Endpoint
        read_only_fields=("id", "name", "owner", "createdAt")
        fields=read_only_fields

class MlAlgoSerializer(serializers.ModelSerializer):
    currentStatus=serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlAlgorithim):
        return MlAlgorithimStatus.objects.filter(parentAlgo=mlAlgorithim).latest('createdAt').status
    
    class Meta:
        model=MlAlgorithim
        read_only_fields=("id", "name", "description", "code", "versions", "owner", "createdAt", "parentEndpoint", "currentStatus")
        fields=read_only_fields

class MlStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=MlAlgorithimStatus
        read_only_fields=("id", "active")
        fields=("id", "active", "status", "createdBy", "createdAt","parentAlgo")

class MlRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=MlRequest
        read_only_fields=("id", "inputData", "fullResponse", "response", "createdAt", "parentMlAlgo")
        fields=("id", "inputData", "fullResponse", "response", "feedback", "createdAt", "parentMlAlgo")