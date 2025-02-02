# Generated by Django 3.1.7 on 2021-04-01 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_articles', to='board.person')),
                ('dislikers', models.ManyToManyField(related_name='dislikes', to='board.Person')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edit_articles', to='board.person')),
                ('likers', models.ManyToManyField(related_name='likes', to='board.Person')),
                ('scrapers', models.ManyToManyField(related_name='scraps', to='board.Person')),
            ],
        ),
    ]
