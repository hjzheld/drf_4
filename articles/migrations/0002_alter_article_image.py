# Generated by Django 4.2.5 on 2023-09-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%n/%d/'),
        ),
    ]
