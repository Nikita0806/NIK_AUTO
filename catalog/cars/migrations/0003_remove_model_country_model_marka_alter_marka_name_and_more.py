# Generated by Django 4.2.2 on 2023-09-19 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_marka_model_person_remove_subject_mar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='country',
        ),
        migrations.AddField(
            model_name='model',
            name='marka',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.marka', verbose_name='Марка:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marka',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Марка:'),
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Модель:'),
        ),
    ]
