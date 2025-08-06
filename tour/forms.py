from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Destination, DestinationImage, Room, Restaurant, Activity, Information  

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'country', 'start_date', 'end_date', 'description', 'map_embed_code']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date cannot be after end date.")


from .models import DestinationImage, Room, Restaurant

class DestinationImageForm(forms.ModelForm):
    class Meta:
        model = DestinationImage
        fields = ['image']



class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'image', 'cost', 'basis', 'nights']
        labels = {
            'name': 'Room Name',
            'description': 'Room Description',
            'image': 'Room Image',
            'cost': 'Accommodation Cost (KSh)',
            'basis': 'Basis (FB/HB/BB)',
            'nights': 'Number of Nights',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'image']
from .models import DestinationImage, Room, Restaurant

class DestinationImageForm(forms.ModelForm):
    class Meta:
        model = DestinationImage
        fields = ['image']


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'image']  


# forms.py

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['content']
