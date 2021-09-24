# Generated by Django 3.2.7 on 2021-09-24 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StickNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
