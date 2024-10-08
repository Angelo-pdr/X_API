# Generated by Django 5.1 on 2024-09-10 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fullName', models.DateTimeField(max_length=150, unique=True)),
                ('nickname', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('user_active', models.BooleanField(default=True)),
                ('user_admi', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
