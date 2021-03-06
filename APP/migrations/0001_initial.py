# Generated by Django 4.0.4 on 2022-04-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oktatasi_azonosito', models.CharField(max_length=30)),
                ('nev', models.CharField(max_length=30)),
                ('pontszam', models.IntegerField(max_length=3)),
                ('Atagozat', models.BooleanField()),
                ('Btagozat', models.BooleanField()),
                ('Ctagozat', models.BooleanField()),
                ('Dtagozat', models.BooleanField()),
                ('Etagozat', models.BooleanField()),
                ('Ftagozat', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Diak',
                'verbose_name_plural': 'Diakok',
            },
        ),
    ]
