# Generated by Django 4.2.4 on 2023-08-31 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0004_alter_author_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.TextField(),
        ),
    ]
