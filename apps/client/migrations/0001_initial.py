# Generated by Django 2.0 on 2020-03-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('client', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='客户端')),
                ('score', models.IntegerField(default=0, verbose_name='分数')),
            ],
            options={
                'verbose_name': '排行榜',
                'verbose_name_plural': '排行榜',
            },
        ),
    ]
