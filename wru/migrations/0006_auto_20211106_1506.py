# Generated by Django 3.2.8 on 2021-11-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wru', '0005_alter_feeling_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='icon',
            field=models.CharField(default='<i class="las la-question-circle"></i>', max_length=100),
        ),
        migrations.AlterField(
            model_name='feeling',
            name='icon',
            field=models.CharField(default='<i class="las la-question-circle"></i>', max_length=100),
        ),
    ]
