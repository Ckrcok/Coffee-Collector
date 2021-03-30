from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Coffee




# coffees = [
#   Coffee('Arabica Coffee', 'Arabica', ' is the most common (and certainly most heavily marketed) type of coffee in North America. That’s because it actually has a sweeter, more delicate flavor and the coffee itself tends to be less acidic.'),
#   Coffee('Robusta Coffee', 'Robusta', 'Robusta coffee beans are second on the list and the most popular in Europe, the Middle East and Africa. Its name does this bean justice, as it is known for its strong and often harsh flavor profile. Robusta coffees have extremely high levels of caffeine, which makes the plant far more resilient than the Arabica species.'),
#   Coffee('Liberica Coffee', 'Liberica', 'Liberica coffee beans are a rare treat. They’re grown in very specific climates with production being far too scarce for farmers to scale their operations to truly satisfy a global marketplace. Even still, the beans are considered a pleasant surprise. Many who’ve tried the coffee liken the aroma to fruit and flowers and describe the flavor as having a somewhat “woody” taste.')
# ]


# Create your views here.
class CoffeeCreate(CreateView):
    model = Coffee
    fields = '__all__'

class CoffeeUpdate(UpdateView):
    model = Coffee
    fields = ['name', 'description', 'type']

class CoffeeDelete(DeleteView):
    model = Coffee
    success_url ='/coffee/'

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')


def coffee_index(request):
    coffees = Coffee.objects.all()
    return render(request,'coffee/index.html', {'coffees':coffees})

def coffees_detail(request, coffee_id):
  coffee = Coffee.objects.get(id=coffee_id)
  return render(request, 'coffee/detail.html', { 'coffee': coffee })
