# Generated by Django 2.1.7 on 2019-02-13 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=60, unique=True)),
                ('wins', models.IntegerField(default=0)),
                ('kills', models.IntegerField(default=0)),
                ('infected', models.IntegerField(default=0)),
            ],
        ),
    ]