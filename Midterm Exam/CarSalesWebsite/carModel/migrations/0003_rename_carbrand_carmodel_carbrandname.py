# Generated by Django 5.0 on 2024-01-05 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carModel', '0002_alter_carmodel_carbrand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='carBrand',
            new_name='carBrandName',
        ),
    ]