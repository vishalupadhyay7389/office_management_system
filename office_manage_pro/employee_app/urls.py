from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index , name='index'),
    path('all/', views.all , name='all'),
    path('addemp/', views.addemp , name='addemp'),
    path('remove_emp/', views.remove_emp , name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp , name='remove_emp'),
    path('filter_emp/', views.filter_emp , name='filter_emp'),
]