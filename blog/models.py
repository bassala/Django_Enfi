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

	