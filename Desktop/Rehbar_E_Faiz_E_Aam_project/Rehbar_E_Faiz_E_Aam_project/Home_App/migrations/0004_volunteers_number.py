# Generated by Django 4.1.4 on 2023-09-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0003_blog_events_volunteers_alter_data_discription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteers',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
