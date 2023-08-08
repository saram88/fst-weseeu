"""django_weseeu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from weseeu import views

urlpatterns = [
     # Open pages
    path('', views.main_view, name='main'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('service/', views.service_view, name='service'),

    # Admin and account
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # Bookings
    path('booking/', views.bookings_view, name='booking'),
    path('booking/add/', views.add_booking, name='add_booking'),
    path('booking/edit/<booking_id>', views.edit_booking, name='edit_booking'),
    path('booking/delete/<booking_id>', views.delete_booking, name='delete_booking'),
    path('booking/profile/', views.edit_profile, name='profile'),
]

handler404 = 'weseeu.views.error_404'
handler500 = 'weseeu.views.error_500'

