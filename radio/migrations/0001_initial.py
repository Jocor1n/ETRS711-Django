# Generated by Django 3.2.5 on 2022-11-21 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=255)),
                ('pub_date', models.DateField(default='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Resistant_has_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudioRadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageCourant_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=45)),
                ('studioRadio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.studioradio')),
            ],
        ),
        migrations.CreateModel(
            name='PosteRadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageCourant_text', models.CharField(max_length=255)),
                ('studioRadio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.studioradio')),
            ],
        ),
        migrations.CreateModel(
            name='GroupeClandestin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=45)),
                ('messageAttendu_text', models.CharField(max_length=255)),
                ('PosteRadio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.posteradio')),
            ],
        ),
        migrations.CreateModel(
            name='Envahisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=45)),
                ('PosteRadio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.posteradio')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_text', models.CharField(max_length=255)),
                ('Message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.message')),
            ],
        ),
    ]