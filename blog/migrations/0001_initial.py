# Generated by Django 2.2.6 on 2019-12-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Стаья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
