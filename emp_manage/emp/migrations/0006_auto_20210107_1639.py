# Generated by Django 3.1.3 on 2021-01-07 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_album_musician'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]