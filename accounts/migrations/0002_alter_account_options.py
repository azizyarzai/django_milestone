# Generated by Django 3.2.5 on 2021-09-22 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'account', 'verbose_name_plural': 'accounts'},
        ),
    ]
