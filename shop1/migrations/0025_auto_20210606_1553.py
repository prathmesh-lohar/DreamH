# Generated by Django 3.2.3 on 2021-06-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0024_auto_20210604_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='poster',
            field=models.ImageField(default='', upload_to='shop1/images/posters'),
        ),
        migrations.AlterField(
            model_name='catgory',
            name='poster',
            field=models.ImageField(default='', upload_to='shop1/images/posters'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimg',
            field=models.ImageField(default='', upload_to='shop1/images'),
        ),
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
        migrations.AlterField(
            model_name='soffer',
            name='poster',
            field=models.ImageField(default='', upload_to='shop1/images/posters'),
        ),
    ]
