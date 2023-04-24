from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, mixins
from django.db import transaction
from rest_framework.exceptions import APIException

# Create your views here.
class EndpointViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class=EndpointSerializer
    queryset=Endpoint.objects.all()

class MlAlgoViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class=MlAlgoSerializer
    queryset=MlAlgorithim.objects.all()

def deactivateoldstatus(instance):
    oldStatus=MlAlgorithimStatus.objects.filter(parentAlgo=instance.parentAlgo, createdAt=instance.createdAt, active=True)
    for i in range(len(oldStatus)):
        oldStatus[i].active=False
        MlAlgorithimStatus.objects.bulk_update(oldStatus, ["active"])

class MLAlgorithmStatusViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = MlStatusSerializer
    queryset = MlAlgorithimStatus.objects.all()
    def performCreate(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                deactivateoldstatus(instance)



        except Exception as e:
            raise APIException(str(e))

class MLRequestViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = MlRequestSerializer
    queryset = MlRequest.objects.all()


