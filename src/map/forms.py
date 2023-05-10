from django import forms
from django.db import models

from .models import User, LandMark, Map

class UserForm(forms.ModelForm):
	username= forms.CharField(
					widget=forms.TextInput(
						attrs={"placeholder": "Your username",
							   "style": "font-size: 4vmin"
						}
					)
				) 
	password= forms.CharField(
					widget=forms.PasswordInput(
						attrs={"placeholder": "Your password",
							   "style": "font-size: 4vmin"
						}
					)
				)

	class Meta:
		model = User
		fields = ['username',
				  'password']

class LandMarkForm(forms.ModelForm):
	name		= forms.CharField(
					widget=forms.TextInput(
						attrs={"placeholder": "Marker name",
							   "style": "font-size: 4vmin"
						}
					)
				) 
	description = forms.CharField(
					widget=forms.Textarea(
						attrs={"placeholder": "Marker description",
							   "style": "font-size: 2vmin"
						}
					)
				) 
	color 		= forms.IntegerField(
				)
	id_on_map   = forms.IntegerField(
					widget=forms.HiddenInput()
				)
	on_map		= forms.IntegerField(
					widget=forms.HiddenInput()
				)
	xcor		= forms.FloatField(
					widget=forms.HiddenInput()
				)
	ycor		= forms.FloatField(
					widget=forms.HiddenInput()
				)

	class Meta:
		model = LandMark
		fields = ['name',
				  'description',
				  "color",
				  'id_on_map',
				  'on_map',
				  'xcor',
				  'ycor']

class MapForm(forms.ModelForm):
	name 	= forms.CharField(
					widget=forms.TextInput(
						attrs={"placeholder": "Marker name",
							   "style": "font-size: 4vmin"
						}
					)
				) 
	image 	= forms.ImageField(required=False)
	on_user	= forms.IntegerField(
					widget=forms.HiddenInput()
				  )
	class Meta:
		model = Map
		fields = ['name',
				  'image',
				  'on_user']