
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about-us/', about, name="about-us"),
    path('services/', services, name="services"),
    path('blogs/', blogs, name="blogs"),
    path('contact-us/', contact, name="contact-us"),
]
