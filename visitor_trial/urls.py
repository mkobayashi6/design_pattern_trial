from django.urls import path

from . import views

app_name = 'visitor_trial'
urlpatterns = [
    # ex: /visitor_trial/
    path('', views.index, name='index'),
    # ex: /visitor_trial/5/
    path('<int:category_id>/', views.detail, name='detail'),
]