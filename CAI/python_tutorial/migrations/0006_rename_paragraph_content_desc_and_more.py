# Generated by Django 5.0.4 on 2024-04-16 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_tutorial', '0005_remove_lesson_heading_remove_lesson_paragraph_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='paragraph',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='heading',
            new_name='title',
        ),
    ]