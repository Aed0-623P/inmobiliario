# Generated by Django 4.2 on 2024-05-07 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("inmobiliaria", "0011_inmueble_comuna_fk_alter_inmueble_comuna"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inmueble",
            name="comuna_fk",
        ),
        migrations.AlterField(
            model_name="inmueble",
            name="comuna",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comuna",
                to="inmobiliaria.comuna",
            ),
        ),
    ]
