# Generated by Django 3.0.6 on 2020-05-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_consumer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='connection',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
