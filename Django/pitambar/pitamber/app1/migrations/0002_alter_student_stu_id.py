# Generated by Django 4.1.6 on 2023-02-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stu_id',
            field=models.IntegerField(),
        ),
    ]
