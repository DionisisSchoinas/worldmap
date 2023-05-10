from django.shortcuts import render, get_object_or_404, redirect

from .models import Map, LandMark
from .forms import MapForm, LandMarkForm

import unicodedata

# Create your views here.
def main_map_view(request, *args, **kwargs):
	cur_map_id = request.session['selected_map']

	cur_map = get_object_or_404(Map, id=cur_map_id)
	marks = LandMark.objects.filter(on_map=cur_map_id)
	
	if request.method == 'POST':
		if 'function' in request.POST:
			mark_id = request.POST['selected_marker']
			map_id = request.POST['on_map']
			#--- Delete Landmark
			if request.POST['function'] == 'delete':
				LandMark.objects.filter(on_map=map_id).filter(id_on_map=mark_id).delete()
				return redirect('./')
			#--- Edit Landmark
			elif request.POST['function'] == 'edit':
				obj = LandMark.objects.filter(on_map=map_id).filter(id_on_map=mark_id)
				obj.update(name=request.POST['mark_name'])
				obj.update(description=request.POST['mark_description'])
				obj.update(color=request.POST['mark_color'])
				obj[0].save();
				return redirect('./')
			#--- Move Landmark
			elif request.POST['function'] == 'move':
				obj = LandMark.objects.filter(on_map=map_id).filter(id_on_map=mark_id)
				obj.update(xcor=request.POST['xcor'])
				obj.update(ycor=request.POST['ycor'])
				obj[0].save()
				return redirect('./')
			#--- Add Landmark
			elif request.POST['function'] == 'add':
				obj = LandMark(
					name=request.POST['mark_name'],
					description=request.POST['mark_description'],
					color=request.POST["mark_color"],
					on_map=map_id,
					id_on_map=mark_id,
					xcor=request.POST['xcor'],
					ycor=request.POST['ycor']
				)
				obj.save()
				return redirect('./')
			#--- Change Map
			elif request.POST['function'] == 'changemap':
				return redirect('./select')
			#--- Logout
			elif request.POST['function'] == 'logout':
				return redirect('../')
			#--- Delete Map
			elif request.POST['function'] == 'deletemap':
				LandMark.objects.filter(on_map=map_id).delete()
				Map.objects.get(id=map_id).delete()
				return redirect('./select')
			#--- Reload Map
			elif request.POST['function'] == 'reload':
				return redirect('./')

	mark_list = []
	for mark in marks:
		mark_list.append(
		{
			"name": mark.name, 
			"description": mark.description, 
			"color": mark.color, 
			"id_on_map": mark.id_on_map, 
			"on_map": mark.on_map, 
			"xcor": mark.xcor, 
			"ycor": mark.ycor
			}
		)

	context = {
		"imageUrl":	cur_map.image.url,
		"width":	cur_map.image.width,
		"height":	cur_map.image.height,
		"landmarks": mark_list,
		"cur_map": cur_map_id,
		"map_name": cur_map.name
	}
	return render(request, "map.html", context)

def map_selection_view(request, *args, **kwargs):
	try:
		del request.session['selected_map']
		request.session.modified = True
	except:
		x=1
		
	cur_user = request.session['user_id']
	user_maps = Map.objects.filter(on_user=cur_user)

	if request.method == 'POST':
		if 'select' in request.POST:
			request.session['selected_map'] = request.POST['selected']
			return redirect('../')
		elif 'cancel' in request.POST:
			return redirect('../../')
		elif 'create' in request.POST:
			return redirect('../create')
	context = {
		'maps': user_maps
	}
	return render(request, "map_selection.html", context)

def map_creation_view(request, *args, **kwargs):
	cur_user = request.session['user_id']
	data = {
		'on_user': cur_user
	}
	form = MapForm(request.POST or None, initial=data)

	if request.method == 'POST':
		if 'cancel' in request.POST:
			return redirect('../select')
		if 'create' in request.POST:
			if form.is_valid():
				Map.objects.create(
					name=form.cleaned_data['name'],
					image=request.FILES['image'],
					on_user=request.session['user_id']
				)
				return redirect('../select')

	context = {
		'form': form
	}
	return render(request, "map_creation.html", context)