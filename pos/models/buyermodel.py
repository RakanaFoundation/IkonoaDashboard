from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=125)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name