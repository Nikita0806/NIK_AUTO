# Generated by Django 4.2.2 on 2023-09-19 10:58

from django.db import migrations
import randomslugfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_cars_name_alter_cars_ls_alter_cars_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='name',
        ),
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=randomslugfield.fields.RandomSlugField(blank=True, editable=False, exclude_lower=True, length=7, max_length=7, unique=True),
        ),
    ]
