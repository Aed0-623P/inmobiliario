# Generated by Django 4.2 on 2024-05-06 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inmobiliaria", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="inmueble",
            name="propietario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="inmobiliaria.usuario",
            ),
        ),
    ]
