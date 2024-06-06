from django.urls import path

from .views import *


app_name = 'main'
urlpatterns = [
    path('', main_page, name="main_page"),
    path('programs/', programs_page, name="programs_page"),
    path('news/', news_page, name="news_page"),
    path('about/', about_page, name="about_page"),
]
