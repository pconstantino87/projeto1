# Generated by Django 4.0.4 on 2022-05-16 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_author_alter_recipe_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tile',
            new_name='title',
        ),
    ]
