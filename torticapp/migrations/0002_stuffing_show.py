# Generated by Django 2.1.2 on 2018-10-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torticapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuffing',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Show or not'),
        ),
    ]
