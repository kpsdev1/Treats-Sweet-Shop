# Generated by Django 3.2.19 on 2023-05-24 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_alter_reviews_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
