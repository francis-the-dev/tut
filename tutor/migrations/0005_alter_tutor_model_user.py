# Generated by Django 5.0.4 on 2025-02-24 07:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_alter_tutor_model_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor_model',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_m', to=settings.AUTH_USER_MODEL),
        ),
    ]
