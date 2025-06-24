from django.db import models

class LostItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_lost = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
