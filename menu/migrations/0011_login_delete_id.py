# Generated by Django 4.1.3 on 2022-12-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='id',
        ),
    ]