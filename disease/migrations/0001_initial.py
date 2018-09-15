# Generated by Django 2.1.1 on 2018-09-15 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=50, verbose_name='疾病名称')),
            ],
            options={
                'verbose_name': 'Disease',
                'verbose_name_plural': 'Diseases',
            },
        ),
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50, verbose_name='分型名称')),
            ],
            options={
                'verbose_name': '疾病分型',
                'verbose_name_plural': '疾病分型',
            },
        ),
        migrations.CreateModel(
            name='MainPrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.CharField(max_length=50, verbose_name='药方')),
            ],
            options={
                'verbose_name': '主方',
                'verbose_name_plural': '主方',
            },
        ),
        migrations.CreateModel(
            name='MainSymptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.CharField(max_length=50, verbose_name='症状')),
            ],
            options={
                'verbose_name': '主症',
                'verbose_name_plural': '主症',
            },
        ),
        migrations.AddField(
            model_name='diseasetype',
            name='add_prescription',
            field=models.ManyToManyField(to='disease.MainPrescription'),
        ),
        migrations.AddField(
            model_name='diseasetype',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.Disease'),
        ),
        migrations.AddField(
            model_name='disease',
            name='main_prescription',
            field=models.ManyToManyField(to='disease.MainPrescription'),
        ),
        migrations.AddField(
            model_name='disease',
            name='main_symptoms',
            field=models.ManyToManyField(to='disease.MainSymptoms'),
        ),
    ]
