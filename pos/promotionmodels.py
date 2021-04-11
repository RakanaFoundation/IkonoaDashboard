from django.db import models
import datetime

class Promotion(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null=True, blank=True)
    dateFrom = models.DateTimeField(auto_now_add=False)
    dateTo = models.DateTimeField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name