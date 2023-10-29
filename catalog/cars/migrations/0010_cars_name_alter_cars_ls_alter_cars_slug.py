# Generated by Django 4.2.2 on 2023-09-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_cars_marka_alter_cars_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cars',
            name='ls',
            field=models.IntegerField(verbose_name='Л.С'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
