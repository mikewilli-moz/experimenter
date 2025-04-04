# Generated by Django 3.0.7 on 2020-10-08 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0119_auto_20201006_1924"),
    ]

    operations = [
        migrations.CreateModel(
            name="NimbusFeatureConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField(max_length=80, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "application",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("firefox-desktop", "Desktop"),
                            ("fenix", "Fenix"),
                            ("reference-browser", "Reference"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("owner_email", models.EmailField(blank=True, max_length=254, null=True)),
                ("schema", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Nimbus Feature Configs",
            },
        ),
        migrations.AddField(
            model_name="nimbusexperiment",
            name="feature_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="experiments.NimbusFeatureConfig",
            ),
        ),
    ]
