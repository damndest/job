from django.shortcuts import render

# Create your views here.
def domestic(request):
    return render(request, 'humor/domestic.html');
