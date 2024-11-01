# Generated by Django 5.1.2 on 2024-11-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0003_remove_case_created_at_remove_case_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="sex",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], max_length=10
            ),
        ),
    ]
