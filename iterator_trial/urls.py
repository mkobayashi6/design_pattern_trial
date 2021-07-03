from django.urls import path

from . import views

app_name = 'iterator_trial'
urlpatterns = [
    # ex: /iterator_trial/
    path('', views.index, name='index'),
    # ex: /iterator_trial/5/
    path('<int:category_id>/', views.detail, name='detail'),
    # ex: /iterator_trial/5/gender
    path('<int:category_id>/gender/', views.gender, name='gender'),
    # ex: /iterator_trial/5/results/
    path('<int:subcategory_id>/results/', views.results, name='results'),
]