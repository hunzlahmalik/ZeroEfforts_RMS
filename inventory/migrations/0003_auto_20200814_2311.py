# Generated by Django 3.1 on 2020-08-14 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200814_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]