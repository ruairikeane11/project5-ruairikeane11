# Generated by Django 4.2.15 on 2024-09-14 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQs'},
        ),
        migrations.RemoveField(
            model_name='faq',
            name='created_on',
        ),
    ]
