from .widgets import  DateTimePickerInput
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    
    class Meta:
        model = Booking
        fields = ['service', 'startdate', 'enddate']

        widgets = {
            'startdate' : DateTimePickerInput(),
            'enddate' : DateTimePickerInput(),
        }