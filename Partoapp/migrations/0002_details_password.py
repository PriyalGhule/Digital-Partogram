# Generated by Django 4.1.3 on 2022-11-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
