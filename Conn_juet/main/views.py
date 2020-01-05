from django.shortcuts import render
from main.models import juetpost
# Create your views here.
def home(request):
	context = {
	   'juetposts': juetpost.objects.all()
	}
	return render(request , 'main/home.html', context)


def about(request):
	return render(request  , 'main/about.html')	