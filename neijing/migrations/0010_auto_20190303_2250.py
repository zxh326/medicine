# Generated by Django 2.1.2 on 2019-03-03 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neijing', '0009_neijingexam_create_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='neijingexam',
            options={'ordering': ['-id'], 'verbose_name': 'exam', 'verbose_name_plural': 'exams'},
        ),
    ]