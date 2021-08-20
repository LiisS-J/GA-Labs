from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TEAS = (
    ("B", "Breakfast Blend"),
    ("G", "Green Tea"),
    ("C", "Chamomile"),
    ("P", "Peppermint"),
)


class Coaster(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("coasters_detail", kwargs={"pk": self.id})


# Create your models here.
class Mug(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    coasters = models.ManyToManyField(Coaster)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"mug_id": self.id})


class Teatime(models.Model):
    date = models.DateField("Choose a Time For Tea")
    tea = models.CharField(max_length=1, choices=TEAS, default=TEAS[0][0])

    mug = models.ForeignKey(Mug, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tea_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
