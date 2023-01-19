from django.db import models


# Create your models here.
class StudioRadio (models.Model):
    messageCourant_text = models.CharField(max_length=255)


class Resistant (models.Model):
    pseudo = models.CharField(max_length=45)
    studioRadio = models.ForeignKey(StudioRadio, on_delete=models.CASCADE)


class PosteRadio (models.Model):
    messageCourant_text = models.CharField(max_length=255)
    studioRadio = models.ForeignKey(StudioRadio, on_delete=models.CASCADE)


class GroupeClandestin (models.Model):
    pseudo = models.CharField(max_length=45)
    messageAttendu_text = models.CharField(max_length=255)
    PosteRadio_id = models.ForeignKey(PosteRadio, on_delete=models.CASCADE)


class Envahisseur (models.Model):
    pseudo = models.CharField(max_length=45)
    PosteRadio_id = models.ForeignKey(PosteRadio, on_delete=models.CASCADE)


class Message (models.Model):
    message_text = models.CharField(max_length=255)
    pub_date = models.DateField(default='date published')


class Action (models.Model):
    action_text = models.CharField(max_length=255)
    Message_id = models.ForeignKey(Message, on_delete=models.CASCADE)


class Resistant_has_Message (models.Model):
    Resistant_idResistant = models.IntegerField(default=1)
    Message_idMessage = models.IntegerField(default=1)
