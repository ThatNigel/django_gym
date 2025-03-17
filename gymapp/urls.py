from django.urls import path
from gymapp import views

urlpatterns = [

    path('', views.index, name='index'),
    path('About/',views.about, name='about'),
    path('Contact/',views.contact, name='contact'),
    path('service/',views.service, name='service'),
    path('login/',views.contact, name='login'),

]