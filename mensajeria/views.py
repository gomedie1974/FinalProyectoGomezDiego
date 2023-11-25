# mensajeria/views.py
from django.shortcuts import render, get_object_or_404
from .models import Chat

def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    usuario_envia = chat.usuario_1
    usuario_recibe = chat.usuario_2

    return render(request, 'mensajeria/chat_detail.html', {'chat': chat, 'usuario_envia': usuario_envia, 'usuario_recibe': usuario_recibe})


""" def chat_detail(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    messages = chat.message_set.order_by('fecha_creacion')
    return render(request, 'mensajeria/chat_detail.html', {'chat': chat, 'messages': messages})
 """
def chat_list(request):
    chats = Chat.objects.all()
    return render(request, 'mensajeria/chat_list.html', {'chats': chats})

 
