# Generated by Django 4.2.4 on 2023-08-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualise', '0006_alter_details_added_alter_details_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='end_year',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='details',
            name='impact',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='details',
            name='relevance',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='details',
            name='start_year',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
