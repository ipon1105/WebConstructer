# Generated by Django 4.1 on 2022-08-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('title', models.CharField(max_length=25)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
