# Generated by Django 3.2.19 on 2023-05-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='post',
        ),
    ]
