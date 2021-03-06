# Generated by Django 2.1.4 on 2018-12-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NeiJingRaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='文章标题')),
                ('raw', models.TextField(verbose_name='原文')),
                ('blank', models.IntegerField(default=0, verbose_name='设置几个填空')),
            ],
            options={
                'verbose_name': 'NeiJingRaw',
                'verbose_name_plural': 'NeiJingRaws',
            },
        ),
    ]
