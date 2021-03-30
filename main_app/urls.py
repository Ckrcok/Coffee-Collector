from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffee/', views.coffee_index, name='index'),
    path('coffee/<int:coffee_id>/', views.coffees_detail, name='detail'),
    path('coffee/create/', views.CoffeeCreate.as_view(), name='coffee_create'),
    path('coffee/<int:pk>/update/', views.CoffeeUpdate.as_view(), name='coffee_update'),
    path('coffee/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffee_delete'),

]
