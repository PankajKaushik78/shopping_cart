# Generated by Django 3.0.5 on 2020-04-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('profiles', '0002_auto_20200425_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='items',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
