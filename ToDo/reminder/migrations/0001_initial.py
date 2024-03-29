# Generated by Django 5.0 on 2023-12-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.CharField(max_length=20)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
