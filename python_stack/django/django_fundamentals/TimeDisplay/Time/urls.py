from django.urls import path

from Time import views

urlpatterns = [
   path('',views.index)
]