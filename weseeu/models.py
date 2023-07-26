from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=30, blank=True)
    company = models.TextField(max_length=50, blank=True)
    address = models.TextField(max_length=50, blank=True)
    postalcode = models.TextField(max_length=10, blank=True)
    city = models.TextField(max_length=30, blank=True)
    country = models.TextField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save() 


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=500, blank=True)
    cost = models.FloatField(default=50)
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="user_service")
    create_on = models.DateTimeField(auto_now_add=True)
    startdate = models.DateTimeField(blank=False)
    enddate = models.DateTimeField(blank=False)
    confirmed = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    """ def _get_total_time(self):
        "Returns the person's full name."
        return '%s, %s %s' % (self.lastname, self.firstname, self.middlename)
    totaltime = property(_get_full_name) """

    class Meta:
        ordering = ["startdate"]

    def __str__(self):
        return self.service.name