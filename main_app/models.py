from django.db import models
from django.urls import reverse
from datetime import date

BOXES = (
    ('N', 'No'),
    ('Y', 'Yes')
)

HEAD = (
    ('PO', 'Pop'),
    ('PH', 'Pop Heroes'),
    ('PA', 'Pop Animation'),
    ('PC', 'Pop Comics'),
    ('PM', 'Pop Movies'),
    ('PT', 'Pop Television'),
)

class Partner(models.Model):
    name = models.CharField(max_length=50)
    item_no = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('partners_detail', kwargs={"pk": self.id})
    
# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    item_no = models.IntegerField()
    description = models.TextField(max_length=250)
    partners = models.ManyToManyField(Partner)

    def __str__(self) -> str:
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pop_id': self.id})
    
    def log_for_today(self):
        return self.logging_set.filter(date=date.today(), opened='N').exists()
    
class Logging(models.Model):
    date = models.DateField('Current Date')
    opened = models.CharField(
        max_length=1,
        choices=BOXES,
        default=BOXES[0][0]
    )
    genre = models.CharField(
        max_length=2,
        choices=HEAD,
        default=HEAD[0][0]
    )
    pop = models.ForeignKey(
        Pop,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.get_genre_display(), self.get_opened_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']