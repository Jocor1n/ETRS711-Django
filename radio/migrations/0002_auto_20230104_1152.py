# Generated by Django 3.2.5 on 2023-01-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resistant_has_message',
            name='message_text',
        ),
        migrations.AddField(
            model_name='resistant_has_message',
            name='Message_idMessage',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='resistant_has_message',
            name='Resistant_idResistant',
            field=models.IntegerField(default=1),
        ),
    ]
