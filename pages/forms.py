from django.forms import ModelForm, Select,	ModelChoiceField, TextInput, NumberInput, Textarea, FileField
from .models import Car, Car_Brand, Car_Model

class AddCarForm(ModelForm):

    class Meta:
        model = Car
        exclude = ['created_date', 'user',]
        labels={
            'car_photo':"Car photo",
            'car_photo_1':"Car photo (optional)",
            'car_photo_2': "Car photo (optional)",
            'car_photo_3':"Car photo (optional)",
            'car_photo_4': "Car photo (optional)",
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder':'Enter title of the advertisments...'}),
            'brand': Select(attrs={'class': 'form-control', 'placeholder': 'Choose brand...'}),
            'model': Select(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price per day'}),
            'body_type': Select(attrs={'class': 'form-control'}),
            'year': NumberInput(attrs={'class':'form-control'}),
            'gearbox': Select(attrs={'class': 'form-control'}),
            'mileage': NumberInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter something about the car...'}),
        }
    

