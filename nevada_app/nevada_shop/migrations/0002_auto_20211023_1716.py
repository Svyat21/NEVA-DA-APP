# Generated by Django 3.2.8 on 2021-10-23 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nevada_shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rider',
            old_name='comment',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='rider',
            old_name='photo',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='rider',
            old_name='about_me',
            new_name='short_description',
        ),
    ]
