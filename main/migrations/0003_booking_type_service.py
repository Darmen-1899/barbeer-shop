# Generated by Django 2.2.6 on 2019-12-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='type_service',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
