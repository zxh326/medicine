# Generated by Django 2.1.2 on 2018-10-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0008_prescription_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='image',
            field=models.ImageField(default='none', upload_to='gif'),
        ),
    ]
