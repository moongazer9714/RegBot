# Generated by Django 4.0.6 on 2022-12-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_userinformation_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user_id',
            field=models.BigIntegerField(blank=True),
        ),
    ]