from django.shortcuts import render

# Create your views here.

def Fun1(request):
    return render(request, 'Fun1.html')

def Fun2(request):
    return render(request, 'Fun2.html')