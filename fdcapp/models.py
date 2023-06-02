from django.db import models
from django.utils import timezone
from django.urls import reverse


class PostRequestCloud(models.Model):

    """
        Classe model do banco de dados que vai armazenar as requests de Cloud
    """
    
    request_id = models.AutoField(primary_key=True)
    solicitante = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now())
    
     
class PostRequestNetwork(models.Model):
    pass
