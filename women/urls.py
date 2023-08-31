from django.urls import path, include

from women.views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
router = DefaultRouter()
router.register(r"women-list", WomenViewSets, basename='women-list')
print(router.urls)

urlpatterns = [

    path('', include(router.urls)),

    # path('women-list/', WomenListAPIView.as_view(), name='women-list'),
    # path('women-list/<int:pk>', WomenAPIView.as_view(), name='women-list'),
    # path('women-create/', WomenCreateAPIView.as_view(), name='women-create'),

]
