from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Booking, Profile, Service
from .forms import BookingForm, UpdateUserForm, UpdateProfileForm
from datetime import datetime
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def main_view(request):
    return render(request, 'index.html')


def service_view(request):
    return render(request, 'services.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


# Error handling
def error_404(request, exception):
        data = {}
        return render(request, '404.html', status=404)


def error_500(request):
        data = {}
        return render(request, '500.html', data)


@login_required
def bookings_view(request):
    if (request.user.is_authenticated):
        if (request.user.is_staff):
            bookings = Booking.objects.all()
        else:
            bookings = Booking.objects.filter(user=request.user.id)

        context = {
            'bookings': bookings
        }
        return render(request, 'bookings.html', context)
    else:
        return redirect('main')


@login_required
def add_booking(request):
    if request.method == 'POST':
        try:
            form = BookingForm(request.POST)
            if form.is_valid():
                # Check if existing booking exist for specified service

                startdate_object = datetime.strptime(
                    request.POST.get('startdate'), '%Y-%m-%d %H:%M')
                enddate_object = datetime.strptime(
                    request.POST.get('enddate'), '%Y-%m-%d %H:%M')

                now = datetime.now()
                if (startdate_object <= now):
                    # Hide confirmed when add booking
                    field = form.fields['confirmed']
                    field.widget = field.hidden_widget()
                    context = {
                        'form': form,
                        'error': 'Start date can not be the same or before current time.'
                    }
                    return render(request, 'add_booking.html', context)

                if (startdate_object >= enddate_object):
                    # Hide confirmed when add booking
                    field = form.fields['confirmed']
                    field.widget = field.hidden_widget()
                    context = {
                        'form': form,
                        'error': 'Start date can not be the same or later then end date.'
                    }
                    return render(request, 'add_booking.html', context)

                if (Booking.get_booking_within_dates(request.POST.get('service'), startdate_object, enddate_object)):
                    # Hide confirmed when add booking
                    field = form.fields['confirmed']
                    field.widget = field.hidden_widget()
                    context = {
                        'form': form,
                        'error': 'Selected booking date is not available for that service. Please select another date or contact us for assistance.'
                    }
                    return render(request, 'add_booking.html', context)

                form.instance.user_id = request.user.id
                form.save()
                messages.success(request, 'Booking added successfully')
                return redirect('booking')
            else:
                # Hide confirmed when add booking
                field = form.fields['confirmed']
                field.widget = field.hidden_widget()
                context = {
                    'form': form,
                    'error': 'Invalid values in booking request'
                }
                return render(request, 'add_booking.html', context)
        except Exception as e:
            form = BookingForm()
            # Hide confirmed when add booking
            field = form.fields['confirmed']
            field.widget = field.hidden_widget()
            context = {
                'form': form,
                'error': 'Exception:' + str(e)
            }
            return render(request, 'add_booking.html', context)
    else:
        form = BookingForm()
        # Hide confirmed when add booking
        field = form.fields['confirmed']
        field.widget = field.hidden_widget()

        context = {
            'form': form,
            'error': ''
        }
        return render(request, 'add_booking.html', context)


@login_required
def edit_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=item)
        if form.is_valid():

            startdate_object = datetime.strptime(request.POST.get('startdate'), '%Y-%m-%d %H:%M')
            enddate_object = datetime.strptime(request.POST.get('enddate'), '%Y-%m-%d %H:%M')

            now = datetime.now()
            if (startdate_object <= now):
                # Hide confirmed when add booking
                field = form.fields['confirmed']
                field.widget = field.hidden_widget()
                context = {
                    'form': form,
                    'error': 'Start date can not be the same or before current time.'
                }
                return render(request, 'add_booking.html', context)

            if (startdate_object >= enddate_object):
                # Hide confirmed when edit booking and user is not 'staff
                if (not request.user.is_staff):
                    field = form.fields['confirmed']
                    field.widget = field.hidden_widget()
                context = {
                    'form': form,
                    'error': 'Start date can not be the same or later then end date.'
                }
                return render(request, 'add_booking.html', context)

            if (Booking.get_booking_within_dates(request.POST.get('service'), startdate_object, enddate_object)):
                # Hide confirmed when edit booking and user is not 'staff'
                if (not request.user.is_staff):
                    field = form.fields['confirmed']
                    field.widget = field.hidden_widget()
                context = {
                    'form': form,
                    'error': 'Selected booking date is not available for that service. Please select another date or contact us for assistance.'
                }
                return render(request, 'edit_booking.html', context)

            form.save()
            messages.success(request, 'Your booking has been updated')
            return redirect('booking')
        else:
            context = {
                'form': form,
                'error': 'Invalid values in booking request'
            }
            return render(request, 'edit_booking.html', context)

    form = BookingForm(instance=item)
    # Show only confirmed when user is 'staff'
    if (not request.user.is_staff):
        field = form.fields['confirmed']
        field.widget = field.hidden_widget()

    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    form = BookingForm(request.POST, instance=booking)
    # form = BookingForm(request.POST, instance=booking, initial={'confirmed': datetime.now().strftime('%Y-%m-%d %H:%M')})
    if request.method == "POST":

        try:
            Booking.set_booking_confirm(booking_id, datetime.now().strftime('%Y-%m-%d %H:%M'))
            messages.success(request, "Booking has been confirmed")
            return redirect('booking')
        except Exception as e:
            context = {
                'form': form,
                'error': 'Exception: ' + str(e)
            }
            return render(request, 'confirm_booking.html', context)

    context = {
        'form': form
    }
    return render(request, 'confirm_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been deleted")
        return redirect('booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'delete_booking.html', context)


@login_required
def edit_profile(request):
    if (request.user.is_authenticated):

        if request.method == "POST":
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='booking')

        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)

        context = {
            'user': user_form,
            'profile': profile_form
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('booking')
