# Generated by Django 4.1.5 on 2023-02-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TickAway', '0006_alter_post_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='icon',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
