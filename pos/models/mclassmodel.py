from django.db import models
from pos.models.departmentmodels import Dept

class Mclass(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=225)
    dept = models.ForeignKey(Dept, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.code