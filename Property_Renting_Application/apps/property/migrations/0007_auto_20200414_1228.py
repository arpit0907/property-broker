# Generated by Django 3.0.2 on 2020-04-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20200414_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interested',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]