from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Coffee, Flavor
from .forms import SugarForm


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
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def coffee_index(request):
    coffees = Coffee.objects.all()
    return render(request,'coffee/index.html', {'coffees':coffees})

def coffees_detail(request, coffee_id):
  coffee = Coffee.objects.get(id=coffee_id)
  flavors_coffee_doesnt_have = Flavor.objects.exclude(id__in = coffee.flavors.all().values_list('id'))
  return render(request, 'coffee/detail.html', { 'coffee': coffee , 'sugar_form' :SugarForm ,'flavors': flavors_coffee_doesnt_have })


def add_sugar(request, coffee_id):

  form = SugarForm(request.POST)

  if form.is_valid():

        new_sugar = form.save(commit=False)
        new_sugar.coffee_id = coffee_id
        new_sugar.save()
  return redirect('detail', coffee_id=coffee_id)

def assoc_flavor(request,coffee_id, flavor_id):
    Coffee.objects.get(id=coffee_id).flavors.add(flavor_id)
    return redirect('detail', coffee_id=coffee_id)

def unassoc_flavor(request,coffee_id, flavor_id):
    Coffee.objects.get(id=coffee_id).flavors.remove(flavor_id)
    return redirect('detail', coffee_id=coffee_id)

class FlavorList(ListView):
    model = Flavor
class FlavorDetail(DetailView):
    model = Flavor
class FlavorCreate(CreateView):
    model = Flavor
    fields='__all__'
class FlavorUpdate(UpdateView):
    model = Flavor
    fields = ['name']

class FlavorDelete(DeleteView):
    model = Flavor
    success_url = '/flavors/'
