from django.db import models

# Create your models here.


class Task(models.Model):
    pri_choices = (
        ('Urgent', 'Urgent'),
        ('Not Urgent', 'Not Urgent')
    )
    st_choices = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    priority = models.CharField(max_length=200, choices=pri_choices)
    status = models.CharField(max_length=10, choices=st_choices, default="Pending")

    def __str__(self):
        return self.name
