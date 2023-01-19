from django import forms


class NomDuFormulaire (forms.Form):
    resistant = forms.CharField(max_length=50)
    message = forms.CharField(max_length=255)


class Change_Message_Courant(forms.Form):
    new_current_message = forms.CharField(max_length=255)


class Supprimer_Message(forms.Form):
    message_a_supprimer = forms.CharField(max_length=255)