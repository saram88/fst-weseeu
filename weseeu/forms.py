from .widgets import  DateTimePickerInput
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

        self.fields['startdate'].widget = forms.widgets.DateTimeInput(
            attrs = {
                'type': 'datetime', 'placeholder': 'yyyy-mm-dd hh:mm',
                'class': 'form-control datetimefield'
                }
            )
        self.fields['enddate'].widget = forms.widgets.DateTimeInput(
            attrs = {
                'type': 'datetime', 'placeholder': 'yyyy-mm-dd hh:mm',
                'class': 'form-control datetimefield'
                }
            )
        self.fields['confirmed'].widget = forms.widgets.DateTimeInput(
            attrs = {
                'type': 'datetime', 'placeholder': 'yyyy-mm-dd hh:mm',
                'class': 'form-control datetimefield'
                }
            )


    class Meta:
        model = Booking
        fields = ['service', 'startdate', 'enddate', 'confirmed', 'description']

        labels = {
            "startdate": "Start date",
            "enddate": "End date",
            "confirmed": "Confirmed date",
            "description": "Add description"
        }

        widgets = {
            'startdate' : DateTimePickerInput(),
            'enddate' : DateTimePickerInput(),
            'confirmed' : DateTimePickerInput(),
        }