# Generated by Django 4.0.6 on 2022-07-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_userinformation_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='region',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
