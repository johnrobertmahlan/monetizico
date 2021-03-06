# Generated by Django 3.1.1 on 2020-10-03 06:25

from django.db import migrations, models
import django_s3_storage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201003_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='img/user.svg', upload_to=django_s3_storage.storage.S3Storage(aws_s3_bucket_name='exchange-2')),
        ),
    ]
