# Generated by Django 2.1.7 on 2019-04-18 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0001_initial'),
        ('formularios', '0002_auto_20190417_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='perguntas',
        ),
        migrations.AddField(
            model_name='formulario',
            name='perguntas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perguntas.Pergunta'),
        ),
    ]
