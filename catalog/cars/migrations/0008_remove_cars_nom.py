# Generated by Django 4.2.2 on 2023-09-19 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_data_obem_priv_pts_sost_top_trans_uchet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='nom',
        ),
    ]