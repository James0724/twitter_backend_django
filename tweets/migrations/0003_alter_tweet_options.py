# Generated by Django 4.0.4 on 2022-05-03 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_remove_tweet_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id'], 'verbose_name': 'Tweet', 'verbose_name_plural': 'Tweets'},
        ),
    ]
