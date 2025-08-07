from django.db import models

class Servicos(models.Model):
    OPCOES_CATEGORIAS = [
        ('SunTrack Services', 'SUNTRACK SERVICES'),
        ('Planos SunTrack', 'PLANOS SUNTRACK'),
        ('GoodWe Services', 'GOODWE SERVICES'),
    ]

    titulo = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to='imagem/%Y/%m/%d', blank=True)
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
