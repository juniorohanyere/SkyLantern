# Generated by Django 4.1.5 on 2023-02-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TickAway', '0004_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(auto_now_add=True, verbose_name='Time'),
        ),
    ]
