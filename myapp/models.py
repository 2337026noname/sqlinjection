from django.db import models

# Create your models here.
class py5test(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name