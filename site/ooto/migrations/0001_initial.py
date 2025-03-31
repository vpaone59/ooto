# Generated by Django 5.1.5 on 2025-02-23 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Choice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=255, unique=True)),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_date", models.DateField()),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_updated", models.DateTimeField(auto_now=True)),
                (
                    "first_choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="first_choice",
                        to="ooto.choice",
                    ),
                ),
                (
                    "second_choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="second_choice",
                        to="ooto.choice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserChoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=255)),
                ("anonymous_name", models.CharField(max_length=255)),
                ("remote_address", models.CharField(max_length=255)),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                (
                    "game_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ooto.game"
                    ),
                ),
                (
                    "user_choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ooto.choice"
                    ),
                ),
            ],
        ),
    ]
