# Generated by Django 4.2.5 on 2023-09-25 12:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
