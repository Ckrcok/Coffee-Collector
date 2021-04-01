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
    path('coffee/<int:coffee_id>/add_sugar/', views.add_sugar, name='add_sugar'),
    path('coffee/<int:coffee_id>/assoc_flavor/<int:flavor_id>', views.assoc_flavor, name='assoc_flavor'),
    path('coffee/<int:coffee_id>/unassoc_flavor', views.unassoc_flavor, name='unassoc_flavor'),
    path('flavors/', views.FlavorList.as_view(), name='flavors_index'),
    path('flavors/<int:pk>/', views.FlavorDetail.as_view(), name='flavors_detail'),
    path('flavors/create/', views.FlavorCreate.as_view(), name='flavors_create'),
    path('flavors/<int:pk>/update/', views.FlavorUpdate.as_view(), name='flavors_update'),
    path('flavors/<int:pk>/delete/', views.FlavorDelete.as_view(), name='flavors_delete'),
]
