# Generated by Django 4.1.7 on 2023-03-03 06:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_alter_contactme_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('website_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_name', models.CharField(choices=[('', '--- Select Social Media ---'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('LinkedIn', 'LinkedIn'), ('YouTube', 'YouTube'), ('Instagram', 'Instagram'), ('Pintarest', 'Pintarest'), ('GitHub', 'GitHub')], max_length=255)),
                ('profile_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Social Account',
                'verbose_name_plural': 'Social Accounts',
                'ordering': ['-id'],
            },
        ),
    ]
