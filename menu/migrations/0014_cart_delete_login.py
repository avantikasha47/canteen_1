# Generated by Django 4.1.3 on 2023-01-07 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0013_rename_password_login_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.burger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
