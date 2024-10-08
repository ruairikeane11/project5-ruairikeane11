# Generated by Django 4.2.15 on 2024-08-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('Xl', 'Extra Large'), ('UK6', 'UK 6'), ('UK7', 'UK 7'), ('UK8', 'UK 8'), ('UK9', 'UK 9'), ('UK10', 'UK 10'), ('UK11', 'UK 11')], max_length=4, null=True),
        ),
    ]
