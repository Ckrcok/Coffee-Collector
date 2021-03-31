from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('contact/', views.about, name='contact'),
    path('coffee/', views.coffee_index, name='index'),
    path('coffee/<int:coffee_id>/', views.coffees_detail, name='detail'),
    path('coffee/create/', views.CoffeeCreate.as_view(), name='coffee_create'),
    path('coffee/<int:pk>/update/', views.CoffeeUpdate.as_view(), name='coffee_update'),
    path('coffee/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffee_delete'),
    path('cats/<int:coffee_id>/add_sugar/', views.add_sugar, name='add_sugar'),

]
