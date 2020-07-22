from django.db import models

# modele todo
class Todo(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()




    def __str__(self):
        return self.title
