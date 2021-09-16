# Generated by Django 3.1.7 on 2021-09-15 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300, unique=True)),
                ('icon', models.CharField(default='las la-question-circle', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('why', models.CharField(blank=True, help_text='Why at this Place?', max_length=500, null=True)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='wru.mood')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='wru.place')),
            ],
        ),
    ]