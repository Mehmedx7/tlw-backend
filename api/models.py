from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty_level = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Hard', 'Hard')])
    image = models.ImageField(upload_to='packages/images/')

    def __str__(self):
        return self.name
