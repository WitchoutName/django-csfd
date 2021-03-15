from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def top10(request):
    return render(request, "top10.html")
