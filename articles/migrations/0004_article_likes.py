# Generated by Django 4.2.5 on 2023-09-25 11:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_alter_article_image_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
