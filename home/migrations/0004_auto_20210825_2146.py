# Generated by Django 3.2.6 on 2021-08-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_problem_primarykey'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='Input',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='Output',
            field=models.TextField(default=0),
        ),
    ]