# Generated by Django 5.0.4 on 2024-04-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_tutorial', '0014_alter_content_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]