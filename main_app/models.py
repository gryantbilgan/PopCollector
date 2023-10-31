from django.db import models

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    item_no = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self) -> str:
        return f'{self.name} ({self.id})'