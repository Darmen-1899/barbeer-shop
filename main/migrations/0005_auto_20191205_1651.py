# Generated by Django 2.2.6 on 2019-12-05 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191205_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='type_service',
            new_name='service',
        ),
    ]
