# Generated by Django 3.0.7 on 2020-10-16 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Peliculas', '0004_auto_20201013_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpeliculas',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
