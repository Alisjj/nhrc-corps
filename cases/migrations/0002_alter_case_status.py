# Generated by Django 5.1.2 on 2024-10-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Active"), (2, "Pending Review"), (3, "Resolved")],
                default=2,
            ),
        ),
    ]