# Generated by Django 5.1.4 on 2025-01-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_contact_github_contact_linkedin_contact_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_projects',
            name='project_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
