# Generated by Django 5.1.2 on 2024-10-24 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_company_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job',
            unique_together={('title', 'company')},
        ),
    ]