# Generated by Django 4.1.7 on 2023-04-04 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=10000)),
                ('file', models.FileField(max_length=250, null=True, upload_to='files/')),
            ],
        ),
    ]
