# Generated by Django 3.1 on 2020-08-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0008_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='title'),
        ),
    ]
