# Generated by Django 2.1.1 on 2018-09-25 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
            },
        ),
        migrations.CreateModel(
            name='CaseSymptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.Case')),
            ],
            options={
                'verbose_name': 'CaseSymptoms',
                'verbose_name_plural': 'CaseSymptomss',
            },
        ),
        migrations.CreateModel(
            name='CaseTyping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.Case')),
            ],
            options={
                'verbose_name': 'CaseTyping',
                'verbose_name_plural': 'CaseTypings',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=50, verbose_name='疾病名称')),
            ],
            options={
                'verbose_name': '疾病',
                'verbose_name_plural': '疾病',
            },
        ),
        migrations.CreateModel(
            name='DiseaseTyping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50, verbose_name='分型名称')),
                ('type_symptoms', models.CharField(max_length=200, verbose_name='分型症状')),
            ],
            options={
                'verbose_name': '疾病分型',
                'verbose_name_plural': '疾病分型',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.CharField(max_length=50, unique=True, verbose_name='药方')),
            ],
            options={
                'verbose_name': '主方',
                'verbose_name_plural': '主方',
            },
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.CharField(max_length=50, unique=True, verbose_name='症状')),
            ],
            options={
                'verbose_name': '主症',
                'verbose_name_plural': '主症',
            },
        ),
        migrations.AddField(
            model_name='diseasetyping',
            name='add_prescription',
            field=models.ManyToManyField(to='disease.Prescription', verbose_name='处方加减'),
        ),
        migrations.AddField(
            model_name='diseasetyping',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.Disease', verbose_name='疾病'),
        ),
        migrations.AddField(
            model_name='disease',
            name='main_prescription',
            field=models.ManyToManyField(blank=True, to='disease.Prescription', verbose_name='主药方'),
        ),
        migrations.AddField(
            model_name='disease',
            name='main_symptoms',
            field=models.ManyToManyField(to='disease.Symptoms', verbose_name='主要症状'),
        ),
        migrations.AddField(
            model_name='casetyping',
            name='typing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='disease.DiseaseTyping'),
        ),
        migrations.AddField(
            model_name='casesymptoms',
            name='symptoms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='disease.Symptoms'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.Disease'),
        ),
        migrations.AddField(
            model_name='case',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AlterUniqueTogether(
            name='casetyping',
            unique_together={('case', 'typing')},
        ),
        migrations.AlterUniqueTogether(
            name='casesymptoms',
            unique_together={('case', 'symptoms')},
        ),
    ]
