# Generated by Django 4.2.6 on 2023-10-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='emalil',
            new_name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='dn1',
            field=models.CharField(default='', max_length=10),
        ),
    ]
