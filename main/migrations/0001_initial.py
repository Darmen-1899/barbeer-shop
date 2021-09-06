# Generated by Django 2.2.6 on 2019-12-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.TextField(max_length=150)),
                ('img', models.ImageField(max_length=150, upload_to='')),
                ('price', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
    ]
