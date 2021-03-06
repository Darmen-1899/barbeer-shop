# Generated by Django 2.2.6 on 2019-12-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_booking_type_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='type_service',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
