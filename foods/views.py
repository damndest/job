from django.shortcuts import render

# Create your views here.
def foods_area(request):
    return render(request, 'area.html');