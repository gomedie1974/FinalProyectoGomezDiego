# mensajeria/models.py
from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    usuario_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_usuario_1')
    usuario_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_usuario_2')

    def __str__(self):
        return f"{self.usuario_1} ({self.usuario_2})"


class Message(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
 
    def __str__(self):
        return f"{self.fecha_creacion} ({self.texto}) ({self.chat})"
  