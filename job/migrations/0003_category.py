# Generated by Django 3.0.7 on 2020-06-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200612_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]