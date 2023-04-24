from django.db import models

# Create your models here.
class Endpoint(models.Model):
    name=models.CharField(max_length=100)
    owner=models.CharField(max_length=100)
    createdAt=models.DateTimeField(auto_now_add=True, blank=True)

class MlAlgorithim(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    code=models.CharField(max_length=50000)
    versions=models.CharField(max_length=100)
    createdAt=models.DateTimeField(auto_now_add=True, blank=True)
    parentEndpoint=models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MlAlgorithimStatus(models.Model):
    status=models.CharField(max_length=100)
    active=models.BooleanField()
    createdBy=models.CharField(max_length=100)
    createdAt=models.DateTimeField(auto_now_add=True, blank=True)
    parentAlgo=models.ForeignKey(MlAlgorithim, on_delete=models.CASCADE, related_name="status")

class MlRequest(models.Model):
    inputData=models.CharField(max_length=10000)
    fullResponse=models.CharField(max_length=10000)
    response=models.CharField(max_length=10000)
    feedback=models.CharField(max_length=1000, blank=True, null=True)
    createdAt=models.DateTimeField(auto_now_add=True, blank=True)
    parentMlAlgo=models.ForeignKey(MlAlgorithim, on_delete=models.CASCADE)
