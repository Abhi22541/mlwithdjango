# Generated by Django 4.2 on 2023-04-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlalgorithim',
            name='owner',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
