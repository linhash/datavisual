# Generated by Django 3.0 on 2020-01-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NbGdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(blank=True, max_length=10, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('num', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nb_gdp',
                'managed': False,
            },
        ),
    ]
