# Generated by Django 4.1.7 on 2023-03-03 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_alter_contactme_options_alter_contactme_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
