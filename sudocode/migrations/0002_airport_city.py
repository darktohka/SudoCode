# Generated by Django 2.1.3 on 2018-11-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudocode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
