from django.db import models

# Create your models here.
class Staff(models.Model):
    DIRECTOR = 'director'
    MARKETING_MANAGER = 'marketing_manager'
    SELLES_MANAGER = 'selles_manager'
    HR = 'hr'

    TAG=(
        ('Director', DIRECTOR),
        ('Marketing Manager', MARKETING_MANAGER),
        ('Selles Manager', SELLES_MANAGER),
        ('HR', HR),
    )


    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=28)
    staff_image = models.ImageField(null=True, blank=True, upload_to='staffs_images/')
    position = models.CharField(max_length=60, choices=TAG)

    def __str__(self):
        return self.firstname

class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to='services_images/')

    def __str__(self):
        return self.name
