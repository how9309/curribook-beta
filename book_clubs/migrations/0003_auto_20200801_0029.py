# Generated by Django 3.0.6 on 2020-07-31 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_clubs', '0002_auto_20200731_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookreviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
