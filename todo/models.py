from django.db import models
from django.contrib.auth.models import User
# modele todo
class Todo(models.Model):
    title=models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #date exact creation
    datecompleted= models.DateTimeField(null=True)

    #boolean for important ,or not choice
    important= models.BooleanField(default=False)

    #user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
