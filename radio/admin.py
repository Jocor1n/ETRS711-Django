from django.contrib import admin

# Register your models here.
from .models import StudioRadio, PosteRadio, Resistant, GroupeClandestin, Envahisseur, Message, Action, Resistant_has_Message

admin.site.register(StudioRadio)
admin.site.register(PosteRadio)
admin.site.register(Resistant)
admin.site.register(GroupeClandestin)
admin.site.register(Envahisseur)
admin.site.register(Message)
admin.site.register(Action)
admin.site.register(Resistant_has_Message)