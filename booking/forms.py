from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tee_time']
        widgets = {
            'tee_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
