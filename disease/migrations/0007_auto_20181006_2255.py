# Generated by Django 2.1.2 on 2018-10-06 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0006_favlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favlist',
            name='fa_disease',
        ),
        migrations.AddField(
            model_name='favlist',
            name='fa_case',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='disease.Case'),
            preserve_default=False,
        ),
    ]
