# Generated by Django 2.1.2 on 2018-10-06 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_auto_20181006_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseTyping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'CaseTyping',
                'verbose_name_plural': 'CaseTypings',
            },
        ),
        migrations.RemoveField(
            model_name='case',
            name='case_typing',
        ),
        migrations.AddField(
            model_name='casetyping',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.Case'),
        ),
        migrations.AddField(
            model_name='casetyping',
            name='typing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='disease.DiseaseTyping'),
        ),
        migrations.AlterUniqueTogether(
            name='casetyping',
            unique_together={('case', 'typing')},
        ),
    ]
