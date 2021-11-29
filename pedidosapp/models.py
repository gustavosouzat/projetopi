from django.db import models

# Create your models here.
class Pedido(models.Model):
    """retorna um representação de um string """
    nome_pedido = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    Pedido = models.CharField(max_length=400, null = True)
    valor_pedido = models.CharField(max_length=200)
    endere_pedido = models.CharField(max_length=200)


    def __str__(self):
        """retorna um representação de um string do modelo"""
        return self.nome_pedido 