# Generated by Django 5.0.1 on 2024-01-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="intraId",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="preferred_language",
            field=models.CharField(
                choices=[("en", "English"), ("ko", "한국어"), ("zh", "中文")],
                default="ko",
                max_length=2,
            ),
        ),
    ]
