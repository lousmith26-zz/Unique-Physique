from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def memberships(request):
    return render(request, 'main/memberships.html')

def training(request):
    return render(request, 'main/training.html')

def services(request):
    return render(request, 'main/services.html')
