# Generated by Django 3.2.12 on 2023-11-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=3000)),
            ],
        ),
    ]
