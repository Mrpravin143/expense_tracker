# Generated by Django 5.2.1 on 2025-05-31 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_author_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
