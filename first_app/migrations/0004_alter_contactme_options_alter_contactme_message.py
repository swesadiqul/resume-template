# Generated by Django 4.1.7 on 2023-03-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_contactme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactme',
            options={'verbose_name_plural': 'Contact Me'},
        ),
        migrations.AlterField(
            model_name='contactme',
            name='message',
            field=models.TextField(),
        ),
    ]
