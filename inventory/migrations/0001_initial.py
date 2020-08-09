# Generated by Django 3.1 on 2020-08-09 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField()),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory_product_created', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory_product_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
