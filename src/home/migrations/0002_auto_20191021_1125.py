# Generated by Django 2.2.6 on 2019-10-21 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alco',
            options={'ordering': ['name'], 'verbose_name_plural': 'alco'},
        ),
    ]
