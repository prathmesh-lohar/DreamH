# Generated by Django 3.2 on 2021-05-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0016_auto_20210502_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimg2',
            field=models.ImageField(blank=True, default='/media/shop1/images/default-image.jpg', null=True, upload_to='shop1/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimg3',
            field=models.ImageField(blank=True, default='/media/shop1/images/default-image.jpg', null=True, upload_to='shop1/images'),
        ),
    ]
