# Generated by Django 4.0.2 on 2022-02-05 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('island', '0004_rename_category_project_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category_name',
            new_name='category',
        ),
    ]