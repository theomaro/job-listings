# Generated by Django 5.1.2 on 2024-10-21 11:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cover_letter',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]