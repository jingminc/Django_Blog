# Generated by Django 4.1.2 on 2022-10-15 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_profile_website_url_profile_facebook_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Website_url',
            new_name='website_url',
        ),
    ]
