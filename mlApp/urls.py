from django.urls import path, include

from . import views

# from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from mlApp.views import EndpointViewSet, PredictView
from mlApp.views import MLAlgorithmViewSet
from mlApp.views import MLAlgorithmStatusViewSet
from mlApp.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path('', include(router.urls)),
    path('<str:endpoint_name>/predict/', PredictView.as_view())
]

# urlpatterns = [
#     path('endpoints/', views.EndpointViewSet.as_view()),
#     path('mlalgorithms/', views.MLAlgorithmViewSet.as_view()),
#     path('mlalgorithmstatuses/', views.MLAlgorithmStatusViewSet.as_view()),
#     path('mlrequests/', views.MLRequestViewSet.as_view()),
    
# ]


