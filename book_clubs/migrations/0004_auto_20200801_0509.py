# Generated by Django 3.0.6 on 2020-07-31 20:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_clubs', '0003_auto_20200801_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
