# Generated by Django 5.1.dev20240507180602 on 2024-06-19 03:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0004_alter_accountuser_account_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountuser",
            name="account_user_id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="accountuser",
            name="account_user_updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]