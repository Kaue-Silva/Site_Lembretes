from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lembrete(models.Model):
    titulo = models.CharField(max_length=30, default='Sem Titulo')
    descricao = models.TextField(blank=True, null=True)
    data_hora = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name_plural = 'Lembretes'

    
    def __str__(self):
        return self.titulo