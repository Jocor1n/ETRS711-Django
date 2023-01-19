from django.http import HttpResponse
from django.template import loader
from .models import StudioRadio, PosteRadio, Resistant, Message, Resistant_has_Message, Action, GroupeClandestin, Envahisseur
from .forms import NomDuFormulaire, Change_Message_Courant, Supprimer_Message
from datetime import datetime
from django.template.defaultfilters import date
from django.shortcuts import redirect
from django.db import connection


def index(request):
    return HttpResponse("Master1 ISC TR - ETRS701_TRI Conception et programmation orientée objet - Christophe Courtin")


# vue studio de radio
def studioRadio(request):
    # Pour Changer le message courant
    if request.method == 'POST' and 'change' in request.POST:
        form = Change_Message_Courant(request.POST)
        if form.is_valid():
            current_message = form.cleaned_data['new_current_message']
            StudioRadio.objects.update(messageCourant_text=current_message)
            # Rediriger vers la même URL après avoir soumis le formulaire
            return redirect('/radio-londres')
    # Pour ajouter un message
    elif request.method == 'POST' and 'add_message' in request.POST:
        form = NomDuFormulaire(request.POST)
        # vérifier si elle est valide
        if form.is_valid():
            message = form.cleaned_data['message']
            resistant = form.cleaned_data['resistant']
            current_date = date(datetime.now(), "Y-m-d")
            if Message.objects.filter(message_text=message).count() == 0 :
                Message.objects.create(message_text=message, pub_date=current_date)
                message_obj = Message.objects.get(message_text=message).id
                resistant_obj = Resistant.objects.get(pseudo=resistant).id
                Resistant_has_Message.objects.create(Resistant_idResistant=resistant_obj, Message_idMessage=message_obj)
                return redirect('/radio-londres')
            else: 
                return HttpResponse("Le Message existe déjà")
        else:
            return HttpResponse("Le formulaire n'est pas valide.")
    # Pour diffuser le message courant sur tous les postes
    elif request.method == 'POST' and 'diffuse' in request.POST:
        new_mes = StudioRadio.objects.first().messageCourant_text
        PosteRadio.objects.update(messageCourant_text=new_mes)
        return redirect('/radio-londres')    
    # Pour supprimer un message
    elif request.method == 'POST' and 'supprimer' in request.POST:
        form = Supprimer_Message(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message_a_supprimer']
            id_a_conserver = Message.objects.get(message_text=message).id
            Message.objects.filter(message_text=message).delete()
            Resistant_has_Message.objects.filter(Message_idMessage=id_a_conserver).delete()
        return redirect('/radio-londres')
    # Requête SQL 
    sql_query = my_custom_sql()
    template = loader.get_template('radio/studioRadio.html')
    context = {'message_courant': StudioRadio.objects.first().messageCourant_text, 'liste_resistants': Resistant.objects.all(), 'liste_message_resistant':sql_query, 'liste_messages': Message.objects.all()}
    return HttpResponse(template.render(context, request))


# vue poste de radio
def posteRadio(request, pseudo):
    template = loader.get_template('radio/posteRadio.html')
    group = ""
    if pseudo == 3:
        group = "Ventriloquist"
    elif pseudo == 4:
        group = "Allemands"
    context = {'pseudo': pseudo, 'message_courant': PosteRadio.objects.get(id=pseudo).messageCourant_text, 'group': group}
    return HttpResponse(template.render(context, request))

# querytest =  PosteRadio.objects.all()
# print(str(querytest.query))
# PosteRadio.objects.filter(id=pseudo)
# traitement associé au formulaire d'appel


def Ventriloquist(request):
    template = loader.get_template('radio/ventriloquist.html')
    message_attendu = GroupeClandestin.objects.get(pseudo="Ventriloquist").messageAttendu_text
    message_ecoute = PosteRadio.objects.get(id=3).messageCourant_text
    action = ""
    if message_attendu == message_ecoute:
        action = "reçoivent le bon message, les saboteurs vont être prevenus"
    else:
        action = "reçoivent un mauvais message"
    context = {'msg_attendu': message_attendu, 'msg_ecoute': message_ecoute, 'action': action}
    return HttpResponse(template.render(context, request))


def Allemands(request):
    template = loader.get_template('radio/Allemands.html')
    context = {'msg_ecoute': PosteRadio.objects.get(id=4).messageCourant_text}
    return HttpResponse(template.render(context, request))


def my_custom_sql():
    cursor = connection.cursor()
    rows = cursor.execute("SELECT r.pseudo, m.message_text FROM 'radio_message' AS m JOIN 'radio_resistant_has_message' AS rhm ON m.id=rhm.Message_idMessage JOIN 'radio_resistant' AS r ON r.id=rhm.Resistant_idResistant")
    rows = cursor.fetchall()
    return rows