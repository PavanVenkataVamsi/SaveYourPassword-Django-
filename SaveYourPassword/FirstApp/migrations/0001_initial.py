# Generated by Django 3.1 on 2020-09-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('gitu', models.CharField(blank=True, max_length=30)),
                ('gitpas', models.CharField(blank=True, max_length=50)),
                ('faceu', models.CharField(blank=True, max_length=30)),
                ('pfacepas', models.CharField(blank=True, max_length=50)),
                ('instau', models.CharField(blank=True, max_length=30)),
                ('stau', models.CharField(blank=True, max_length=30)),
                ('instapas', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
