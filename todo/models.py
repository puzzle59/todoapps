from django.db import models

# modele todo
class Todo(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()

    #test pour le choix multiple:
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES , default='S')
#issue documentation


    def __str__(self):
        return self.title
