# Generated by Django 3.2.3 on 2021-05-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210527_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
