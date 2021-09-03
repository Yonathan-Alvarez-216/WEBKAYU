from django.shortcuts import render

# Create your views here.
def astra(request):
    return render(request, 'index.html')
def astra2(request):
    return render(request, 'Part2.html')
