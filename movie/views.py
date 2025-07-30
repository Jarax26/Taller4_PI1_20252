from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Tomás Jaramillo Gaviria'})
def about(request):
    return HttpResponse('<h1>About Movie Reviews</h1><p>This is a platform for movie enthusiasts to share their reviews and ratings.</p>')