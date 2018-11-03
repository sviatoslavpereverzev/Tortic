# Generated by Django 2.1.2 on 2018-10-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torticapp', '0005_auto_20181022_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuffing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(max_length=500, verbose_name='About stuffing')),
                ('image', models.ImageField(upload_to='', verbose_name='Image stuffing')),
                ('order', models.PositiveIntegerField(verbose_name='Output order')),
            ],
            options={
                'verbose_name': 'Stuffing',
                'verbose_name_plural': 'Stuffing',
            },
        ),
    ]
