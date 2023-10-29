# Generated by Django 4.2.2 on 2023-09-19 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_remove_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuzov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuzov', models.CharField(max_length=40, verbose_name='Тип кузова:')),
            ],
            options={
                'verbose_name': 'Тип кузова',
                'verbose_name_plural': 'Тип кузова',
            },
        ),
        migrations.AlterField(
            model_name='cars',
            name='cuzov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.cuzov', verbose_name='Тип кузова:'),
        ),
    ]
