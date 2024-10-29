from django.db import models
from django.urls import reverse # new

# Create your models here.
class Golfclub(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    year_established = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('c_detail', args=[str(self.id)])

class Member(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    golfclub = models.ForeignKey(
        Golfclub,
        on_delete=models.CASCADE,
    )
    handicap = models.IntegerField()

    def __str__(self):
        return self.name
    

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    golfclub = models.ForeignKey(
        Golfclub,
        on_delete=models.CASCADE,
    ) 
    

    def __str__(self):
        return self.name
    
