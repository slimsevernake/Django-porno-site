# Generated by Django 3.1.4 on 2021-04-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20210402_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='rating',
            field=models.FloatField(blank=True, default=0, max_length=100, verbose_name='Рейтинг'),
        ),
    ]
