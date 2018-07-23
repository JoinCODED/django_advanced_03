from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name