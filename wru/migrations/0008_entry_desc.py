# Generated by Django 3.2.8 on 2021-11-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wru', '0007_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='desc',
            field=models.TextField(blank=True, help_text='description', null=True),
        ),
    ]