# Generated by Django 4.2.4 on 2023-08-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='added',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='end_year',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='impact',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='insight',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='intensity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='likelihood',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='pestle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='published',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='region',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='relevance',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='sector',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='source',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='start_year',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='topic',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
