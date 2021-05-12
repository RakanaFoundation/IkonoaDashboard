from django.db import models

class DeptGrup(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class Dept(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=125)
    deptGroup = models.ForeignKey(DeptGrup, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

