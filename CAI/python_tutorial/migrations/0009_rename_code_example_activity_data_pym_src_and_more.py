# Generated by Django 5.0.4 on 2024-04-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_tutorial', '0008_alter_activity_code_example_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='code_example',
            new_name='data_pym_src',
        ),
        migrations.AddField(
            model_name='activity',
            name='script_src',
            field=models.TextField(blank=True, null=True),
        ),
    ]