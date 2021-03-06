from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


SUGARS =(
('White ', 'White '),
('Brown', 'Brown'),
('Stevia', 'Stevia'),
('Coconut',"Coconut")
)

# Create your models here.
class Flavor(models.Model):
    name = models.CharField(max_length = 50)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flavors_detail', kwargs={'pk':self.id})


class Coffee(models.Model):
    name = models.CharField(max_length=(100))
    type = models.CharField(max_length=(100))
    description = models.TextField(max_length=400)

    flavors = models.ManyToManyField(Flavor)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coffee_id' : self.id})

class Sugar(models.Model):
    type = models.CharField(max_length=(8), choices=(SUGARS), default=SUGARS[0][0])
    amount = models.IntegerField()
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_suger_display()} on{self.date}"

        class Meta:
            ordering = ['-date']
