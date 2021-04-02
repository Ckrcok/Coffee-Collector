from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Coffee, Flavor
from .forms import SugarForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
class CoffeeCreate(LoginRequiredMixin, CreateView):
    model = Coffee
    fields = '__all__'
      # This inherited method is called when a
  # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

@login_required
class CoffeeUpdate(LoginRequiredMixin, UpdateView):
    model = Coffee
    fields = ['name', 'description', 'type']

@login_required
class CoffeeDelete(LoginRequiredMixin, DeleteView):
    model = Coffee
    success_url ='/coffee/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def coffee_index(request):
    coffees = Coffee.objects.all()
    return render(request,'coffee/index.html', {'coffees':coffees})
@login_required
def coffees_detail(request, coffee_id):
  coffee = Coffee.objects.get(id=coffee_id)
  flavors_coffee_doesnt_have = Flavor.objects.exclude(id__in = coffee.flavors.all().values_list('id'))
  return render(request, 'coffee/detail.html', { 'coffee': coffee , 'sugar_form' :SugarForm ,'flavors': flavors_coffee_doesnt_have })

@login_required
def add_sugar(request, coffee_id):

  form = SugarForm(request.POST)

  if form.is_valid():

        new_sugar = form.save(commit=False)
        new_sugar.coffee_id = coffee_id
        new_sugar.save()
  return redirect('detail', coffee_id=coffee_id)

@login_required
def assoc_flavor(request,coffee_id, flavor_id):
    Coffee.objects.get(id=coffee_id).flavors.add(flavor_id)
    return redirect('detail', coffee_id=coffee_id)

@login_required
def unassoc_flavor(request,coffee_id, flavor_id):
    Coffee.objects.get(id=coffee_id).flavors.remove(flavor_id)
    return redirect('detail', coffee_id=coffee_id)

class FlavorList(LoginRequiredMixin, ListView):
    model = Flavor
class FlavorDetail(LoginRequiredMixin, DetailView):
    model = Flavor
class FlavorCreate(LoginRequiredMixin, CreateView):
    model = Flavor
    fields='__all__'
class FlavorUpdate(LoginRequiredMixin, UpdateView):
    model = Flavor
    fields = ['name']

class FlavorDelete(LoginRequiredMixin, DeleteView):
    model = Flavor
    success_url = '/flavors/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
