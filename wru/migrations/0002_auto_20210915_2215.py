# Generated by Django 3.1.7 on 2021-09-15 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wru', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mood',
            new_name='Feeling',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='mood',
            new_name='feeling',
        ),
    ]
