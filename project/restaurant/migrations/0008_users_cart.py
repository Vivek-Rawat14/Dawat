# Generated by Django 5.0.6 on 2024-07-31 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_users_city_users_email_users_phone_users_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='cart',
            field=models.JSONField(default='{}'),
            preserve_default=False,
        ),
    ]
