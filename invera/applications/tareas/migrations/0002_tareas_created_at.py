# Generated by Django 3.2.2 on 2021-10-17 00:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='fecha creacion'),
            preserve_default=False,
        ),
    ]
