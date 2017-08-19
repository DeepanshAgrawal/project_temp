from django.db import models

class Object(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name