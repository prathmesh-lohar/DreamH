# Generated by Django 3.2 on 2021-04-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0014_auto_20210409_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimg2',
            field=models.ImageField(default=1, upload_to='shop1/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimg3',
            field=models.ImageField(default=1, upload_to='shop1/images'),
        ),
    ]
