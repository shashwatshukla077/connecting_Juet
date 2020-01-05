from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
	return render(request, 'user/register.html' , {'form':form})