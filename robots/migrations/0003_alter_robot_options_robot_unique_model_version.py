# Generated by Django 4.2.5 on 2023-10-01 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("robots", "0002_alter_robot_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="robot",
            options={
                "ordering": ("serial",),
                "verbose_name": "робот",
                "verbose_name_plural": "роботы",
            },
        ),
        migrations.AddConstraint(
            model_name="robot",
            constraint=models.UniqueConstraint(
                fields=("model", "version"), name="unique_model_version"
            ),
        ),
    ]
