from django.shortcuts import render
from .models import Tour

# Create your views here.
def index(request):
    tours = Tour.objects.all()
    context = {'tours':tours} #dictionary that gets all the db values
    return render(request, 'tours/index.html', context)