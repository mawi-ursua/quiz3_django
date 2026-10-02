from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name