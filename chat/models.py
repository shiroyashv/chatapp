from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    user = models.ForeignKey(
        User, verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='contacts',
    )
    contact = models.ForeignKey(
        User, verbose_name=_('contact'),
        on_delete=models.CASCADE,
        related_name='contacted_by',
    )


class ChatRoom(models.Model):
    name = models.CharField(
        _('name'), max_length=255,
    )
    description = models.TextField(
        _('description'), max_length=255,
    )
    members = models.ManyToManyField(
        User, verbose_name=_('members'),
        related_name='chat_rooms',
    )


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='sent_messages',
    )
    recipient = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE,
        related_name='messages',
    )
    content = models.TextField(
        _('content'), max_length=255,
    )
    timestamp = models.DateTimeField(
        _('timestamp'), auto_now_add=True,
    )
