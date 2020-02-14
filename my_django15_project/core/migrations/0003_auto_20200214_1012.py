# Generated by Django 3.0.2 on 2020-02-14 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200214_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postgroup2',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PostGroup2', to=settings.AUTH_USER_MODEL),
        ),
    ]