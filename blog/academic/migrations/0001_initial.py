# Generated by Django 4.1.6 on 2023-02-14 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=20)),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=200)),
                ('source_file', models.FileField(upload_to='')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.subject')),
            ],
        ),
    ]
