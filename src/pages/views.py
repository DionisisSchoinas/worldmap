from django.shortcuts import render, redirect

from map.models import User, Map
from map.forms import UserForm, MapForm

# Create your views here.
def home_view(request, *args, **kwargs):
	request.session.flush()
	request.session.modified = True
	
	form = UserForm(request.POST or None)

	if request.method == 'POST':
		if 'register' in request.POST:
			return redirect('./register')

	if form.is_valid():
		user = User.objects.filter(username=form.cleaned_data['username']).filter(password=form.cleaned_data['password'])
		if len(user) == 1:
			request.session['user_id'] = user[0].id
			return redirect('./map/select')
		else:
			context = {
				'form': form,
				'message': 'Username or password are incorrect'
			}
			return render(request, "login.html", context)
	context = {
		'form': form,
		'message': ''
	}
	return render(request, "login.html", context)

def register_view(request, *args, **kwargs):
	form = UserForm(request.POST or None)
	if request.method == 'POST':
		if 'cancel' in request.POST:
			return redirect('../')

	if form.is_valid():
		user = User.objects.filter(username=form.cleaned_data['username']).filter(password=form.cleaned_data['password'])
		if len(user) == 0:
			form.save()
			return redirect('../')
		else:
			context = {
				'form': form,
				'message': 'User already exists'
			}
			return render(request, "register.html", context)
	context = {
		'form': form,
		'message': ''
	}
	return render(request, "register.html", context)