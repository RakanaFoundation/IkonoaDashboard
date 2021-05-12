from django.db import models

class Measurement(models.Model):
    unit = models.CharField(max_length=10)
    convertion = models.IntegerField()

    def __str__(self):
        return self.unit