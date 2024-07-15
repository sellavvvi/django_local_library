from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('about-us', views.about_us, name="about_us"),
     path('classes', views.classes, name="classes"),
     path('teachers', views.teachers, name="teachers"),
     path('faq', views.faq, name="faq"),
     path('contact-us', views.contact_us, name="contact_us"),
]