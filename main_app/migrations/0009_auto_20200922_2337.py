# Generated by Django 3.1 on 2020-09-22 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200920_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateField(default='2020-10-22'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(choices=[('A', 'Animals'), ('V', 'Vehicles'), ('H', 'Household Goods'), ('F', 'Furniture'), ('E', 'Electronics'), ('C', 'Clothes'), ('J', 'Jewelry'), ('M', 'Makeup'), ('B', 'Books'), ('S', 'Sports')], default='A', max_length=1),
        ),
    ]
