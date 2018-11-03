# Generated by Django 2.1.3 on 2018-11-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('iso_code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('continent', models.CharField(max_length=20)),
            ],
        ),
    ]