# Generated by Django 4.0.5 on 2022-07-15 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_category_servicecategory_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceCategory',
            new_name='Category',
        ),
    ]
