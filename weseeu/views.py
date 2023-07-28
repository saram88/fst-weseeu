from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Profile, Service
from .forms import BookingForm
from datetime import datetime
from django.utils.dateparse import parse_date


def main_view(request):
    return render(request, 'weseeu/index.html')


def bookings_view(request):
    if (request.user.is_authenticated):
        bookings = Booking.objects.filter(user=request.user.id)
        context = {
            'bookings': bookings
        }  
        return render(request, 'weseeu/bookings.html', context)
    else:
        return redirect('main')


def add_booking(request):
    if request.method == 'POST':
        try:
            form = BookingForm(request.POST)
            if form.is_valid():
                # Check if existing booking exist for specified service

                startdate_object = datetime.strptime(request.POST.get('startdate'), '%Y-%m-%d %H:%M')
                enddate_object = datetime.strptime(request.POST.get('enddate'), '%Y-%m-%d %H:%M')

                #startdate_object = parse_date(request.POST.get('startdate'))  
                #enddate_object = parse_date(request.POST.get('enddate'))
                if (False): #(Booking.get_booking_within_dates(request.POST.get('service'), startdate_object, enddate_object)):
                    # Hide confirmed when add booking
                    field = form.fields['confirmed']
                    field.widget = field.hidden_widget()
                    context = {
                        'form': form,
                        'error': 'Selected booking date is not available for that service. Please select another date or contact us for assistance.'
                    }    
                    return render(request, 'weseeu/add_booking.html', context)

                form.instance.user_id = request.user.id
                form.save()
                return redirect('booking')
            else:
                #form = BookingForm()
                # Hide confirmed when add booking
                field = form.fields['confirmed']
                field.widget = field.hidden_widget()
                context = {
                    'form': form,
                    'error': 'Invalid values in booking request'
                }
                return render(request, 'weseeu/add_booking.html', context)
        except Exception as e:
            form = BookingForm()
            # Hide confirmed when add booking
            field = form.fields['confirmed']
            field.widget = field.hidden_widget()
            context = {
                'form': form,
                'error': 'Exception:' + str(e)
            }
            return render(request, 'weseeu/add_booking.html', context)
    else:
        form = BookingForm()
        # Hide confirmed when add booking
        field = form.fields['confirmed']
        field.widget = field.hidden_widget()

        context = {
            'form': form,
            'error': ''
        }
        return render(request, 'weseeu/add_booking.html', context)
        

def edit_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('booking')
        else:
            context = {
                'form': form,
                'error': 'Invalid values in booking request'
            }
            return render(request, 'weseeu/edit_booking.html', context)
    
    form = BookingForm(instance=item)
    # Show only confirmed when user is 'staff'
    if (not request.user.is_staff):
        field = form.fields['confirmed']
        field.widget = field.hidden_widget()
    context = {
        'form': form
    }
    return render(request, 'weseeu/edit_booking.html', context)

def delete_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    item.delete()
    return redirect('booking')


def edit_profile(request):
    if (request.user.is_authenticated):
        profile = Profile.objects.filter(user=request.user.id)
        context = {
            'profile': profile
        }  
        return render(request, 'weseeu/profile.html', context)
    else:
        return redirect('booking')
