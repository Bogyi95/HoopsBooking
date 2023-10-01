from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    pin = models.CharField(max_length=4)

    def __str__(self):
        return self.name
