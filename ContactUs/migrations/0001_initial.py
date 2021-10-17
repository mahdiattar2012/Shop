# Generated by Django 2.1.15 on 2021-10-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.TextField(max_length=500)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
