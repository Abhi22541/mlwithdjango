from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
router=DefaultRouter()
router.register(r'endpoints', EndpointViewset, basename='endpoint')
router.register(r'mlalgorithim', MlAlgoViewset, basename='mlalgo')
router.register(r'mlalgostaus', MLAlgorithmStatusViewSet, basename='mlalgostatus')
router.register(r'mlrequests', MLRequestViewSet, basename='mlrequest')

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
