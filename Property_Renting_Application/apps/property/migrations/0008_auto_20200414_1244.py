# Generated by Django 3.0.2 on 2020-04-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20200414_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interested',
            name='approve',
            field=models.BooleanField(null=True),
        ),
    ]