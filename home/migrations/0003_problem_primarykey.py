# Generated by Django 3.2.6 on 2021-08-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_test_case_testcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='primarykey',
            field=models.IntegerField(default=0),
        ),
    ]