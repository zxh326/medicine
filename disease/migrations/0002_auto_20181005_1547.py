# Generated by Django 2.1.2 on 2018-10-05 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseTypingSymptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms_name', models.CharField(max_length=30, verbose_name='分型症状名字')),
            ],
            options={
                'verbose_name': 'DiseaseTypingSymptoms',
                'verbose_name_plural': 'DiseaseTypingSymptomss',
            },
        ),
        migrations.RemoveField(
            model_name='diseasetyping',
            name='type_symptoms',
        ),
        migrations.AddField(
            model_name='diseasetypingsymptoms',
            name='symptoms_typing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.DiseaseTyping', verbose_name='分型'),
        ),
    ]
