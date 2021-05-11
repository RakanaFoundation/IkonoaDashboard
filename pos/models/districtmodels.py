from django.db import models

class District(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.nama_distrik