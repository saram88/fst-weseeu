from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Profile
from .forms import BookingForm

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
                form.instance.user_id = request.user.id
                form.save()
                return redirect('booking')
            else:
                form = BookingForm()
                context = {
                    'form': form,
                    'error': 'Invalid values'
                }
                return render(request, 'weseeu/add_booking.html', context)
        except Exception as e:
            form = BookingForm()
            context = {
                'form': form,
                'error': e
            }
            return render(request, 'weseeu/add_booking.html', context)
    else:
        form = BookingForm()

        field = form.fields['confirmed']
        field.widget = field.hidden_widget()

        context = {
            'form': form
        }
        return render(request, 'weseeu/add_booking.html', context)
        


def edit_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('booking')
    form = BookingForm(instance=item)
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
