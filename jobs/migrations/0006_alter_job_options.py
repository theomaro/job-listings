# Generated by Django 5.1.2 on 2024-10-22 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_company_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['title']},
        ),
    ]
