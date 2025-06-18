from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
