from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('<h1> \(@^0^@)/ </h1>')

def about(request):
    return render(request, 'about.html')
