# Generated by Django 2.1.7 on 2020-01-14 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_comment_parentt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parentt',
        ),
    ]
