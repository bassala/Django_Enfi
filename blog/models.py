from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()
    create_date  = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __str__(self):
        return self.titre
    
class commentaire(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name= 'commentaires')
    nom = models.CharField(max_length=80)
    email = models.EmailField()
    corps = models.TextField()
    created_on =models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
class Meta:
    ordering = ['created_on']
    def __str__(self):
        return 'commentaire{} par {}'.format(self.corps, self.nom)



	