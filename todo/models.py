from django.db import models
from django.contrib.auth.models import User
# modele todo
class Todo(models.Model):
    title = models.CharField(max_length= 100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add= True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important= models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#petite fonction ci desssous sert à afficher le titre de la todo
#dans l'interface admin pour s'y retrouver
    def __str__(self):
        return self.title
