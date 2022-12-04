from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    total = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number}: {self.name}"

    class Meta:
        ordering = ['date_created']
