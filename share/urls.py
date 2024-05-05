from django.urls import path

from . import views

urlpatterns = [
    path('shares', views.ShareView.as_view(), name='shares'),
]