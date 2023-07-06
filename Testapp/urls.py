from django.contrib import admin
from django.urls import path
from Testapp import views


urlpatterns = [
    #path('',views.Hello_World_Fun),
    path('',views.main),
    path('join/', views.join),
    path('login/', views.Login),
    path('home/',views.Return_data),
    path('register/',views.register),
    path('event/',views.event),
    path('upload/',views.upload.as_view())
]
