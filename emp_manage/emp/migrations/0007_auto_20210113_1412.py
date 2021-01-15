# Generated by Django 3.1.3 on 2021-01-13 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_auto_20210107_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentfolder',
            name='documentversions',
        ),
        migrations.RemoveField(
            model_name='documentfolder',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='documentversions',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='documentversions',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='employeedocument',
            name='documentversion',
        ),
        migrations.RemoveField(
            model_name='employeedocument',
            name='employees',
        ),
        migrations.DeleteModel(
            name='EmployeeStatus',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.DeleteModel(
            name='DocumentFolder',
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
        migrations.DeleteModel(
            name='DocumentVersions',
        ),
        migrations.DeleteModel(
            name='EmployeeDocument',
        ),
    ]