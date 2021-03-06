# Generated by Django 3.0.6 on 2020-05-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='Username',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='context',
        ),
        migrations.AddField(
            model_name='consumer',
            name='Broker_ip',
            field=models.GenericIPAddressField(default='127.0.0.1', protocol='IPv4'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='Queue_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='packet_to_consume',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='username',
            field=models.CharField(default='hgh', max_length=50),
        ),
    ]
