from . import views
from django.urls import path

app_name = 'mad_libs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:madlib_id>/', views.get_words, name='get_words'),
    path('<int:madlib_id>/<str:words>', views.mad_lib, name='mad_lib')
]
