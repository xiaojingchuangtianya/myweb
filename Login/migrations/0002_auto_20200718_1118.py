# Generated by Django 2.0.1 on 2020-07-18 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_pro',
            name='Birthday',
            field=models.DateField(blank=True),
        ),
    ]
