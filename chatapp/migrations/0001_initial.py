# Generated by Django 4.2.1 on 2024-01-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChatMessage",
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
                ("bot", models.CharField(max_length=255)),
                ("conversation_id", models.CharField(max_length=100)),
            ],
        ),
    ]
