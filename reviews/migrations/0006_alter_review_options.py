# Generated by Django 3.2.19 on 2023-05-26 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230524_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date_added'], 'verbose_name_plural': 'Reviews'},
        ),
    ]
