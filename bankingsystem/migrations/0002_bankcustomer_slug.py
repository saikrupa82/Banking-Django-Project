# Generated by Django 3.0.5 on 2021-02-14 06:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bankingsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankcustomer',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
