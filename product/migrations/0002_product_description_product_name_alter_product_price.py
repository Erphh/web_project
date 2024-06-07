# Generated by Django 5.0.4 on 2024-05-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='desc', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='price', max_length=10),
        ),
    ]
