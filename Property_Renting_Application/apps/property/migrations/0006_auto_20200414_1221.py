# Generated by Django 3.0.2 on 2020-04-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='interested',
            name='approve',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Approved',
        ),
    ]
