# Generated by Django 2.1.7 on 2020-01-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_blogpost_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='price',
            field=models.IntegerField(default=True),
        ),
    ]
