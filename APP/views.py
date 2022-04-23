from django.shortcuts import render

# Create your views here.

def VIEW(request):
	return render(request, "APP/index.html", {})