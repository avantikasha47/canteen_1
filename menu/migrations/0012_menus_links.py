# Generated by Django 4.1.3 on 2022-12-31 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_login_delete_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus',
            name='links',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
