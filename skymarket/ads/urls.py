from django.urls import path, include
from rest_framework import routers
from ads import views

ads_router = routers.SimpleRouter()
ads_router.register('ads', views.AdvertisementViewSet)
ads_router.register(r'ads/(?P<ad_pk>[^/.]+)/comments', views.CommentsViewSet)

urlpatterns = [
    path('ads/me/', views.AdvertisementsUserOwnerListView.as_view()),
    path('', include(ads_router.urls)),
]

