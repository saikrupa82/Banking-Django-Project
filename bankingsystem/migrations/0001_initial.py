# Generated by Django 3.0.5 on 2021-02-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankcustomer',
            fields=[
                ('firstname', models.CharField(max_length=100)),
                ('EmailId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('lastName', models.CharField(blank=True, max_length=200)),
                ('Balance', models.IntegerField()),
                ('AccountNumber', models.IntegerField()),
            ],
        ),
    ]
