# Generated by Django 5.2.4 on 2025-07-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('firstname', models.CharField(max_length=150, unique=True)),
                ('lastname', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('submitted', models.BooleanField(default=False)),
            ],
        ),
    ]
