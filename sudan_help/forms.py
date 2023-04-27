from django import forms
from django.utils.translation import gettext as _
from .models import Request, MedicalService, MissingPerson #Accommodation, FoodItem, Water, Medicine, Hospital, Pharmacy


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        # fields = ['name', 'address', 'description']


# class MedicalServiceForm(forms.ModelForm):
#     class Meta:
#         model = MedicalService
#         fields = '__all__'
        # fields = ['name', 'address', 'description']


class MedicalServiceForm(forms.ModelForm):

    open_from = forms.DateTimeField(
        label=_('Open from'),
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    closes_at = forms.DateTimeField(
        label=_('Closes at'),
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )


    class Meta:
        model = MedicalService
        fields = '__all__'

class MissingPersonForm(forms.ModelForm):
    class Meta:
        model = MissingPerson
        fields = '__all__'
        widgets = {
            'last_seen_date': forms.DateInput(attrs={'type': 'date'})
        }
