# Generated by Django 4.2.2 on 2023-09-19 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_marka_options_alter_model_options_cars_marka_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
    ]
