# Generated by Django 4.2 on 2024-05-07 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inmobiliaria", "0003_region_comuna"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inmueble",
            name="comuna",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="inmuebles",
                to="inmobiliaria.comuna",
            ),
        ),
    ]
