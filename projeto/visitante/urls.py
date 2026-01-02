from django.urls import path
from . import views


urlpatterns = [
    path('landpage/', views.landpage, name='landpage')
]