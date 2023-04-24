from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register(r'endpoint/', EndpointViewset, basename='endpoint')
router.register(r'mlalgorithim/', MlAlgoViewset, basename='mlalgo')
router.register(r'mlalgostaus/', MLAlgorithmStatusViewSet, basename='mlalgostatus')
router.register(r'mlrequests/', MLRequestViewSet, basename='mlrequest')

urlpatterns=router.urls
