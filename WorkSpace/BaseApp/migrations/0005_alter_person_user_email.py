# Generated by Django 4.1.4 on 2023-01-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='User_Email',
            field=models.CharField(max_length=50),
        ),
    ]