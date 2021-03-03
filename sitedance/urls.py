from django.urls import path

from sitedance import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('sport', views.sport_view, name='sport'),
    path('covid-19', views.covid_view, name='covid-19'),
    path('contacts', views.contacts_view, name='contacts'),
    path('about', views.about_view, name='about'),
    path('achievements', views.achievements_view, name='achievements'),
    path('info', views.info_view, name='info'),
    path('appointment', views.appointment_view, name='appointment')
]
