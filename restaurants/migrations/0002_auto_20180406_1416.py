# Generated by Django 2.0.4 on 2018-04-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='course',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
