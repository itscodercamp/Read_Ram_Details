# Generated by Django 4.1.4 on 2023-09-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TableApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]