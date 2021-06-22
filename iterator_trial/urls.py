from django.urls import path

from . import views

urlpatterns = [
    # ex: /iterator_trial/
    path('', views.index, name='index'),
    # ex: /iterator_trial/5/
    path('<int:category_id>/', views.detail, name='detail'),
]