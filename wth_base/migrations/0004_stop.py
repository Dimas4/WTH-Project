# Generated by Django 2.1.3 on 2018-11-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wth_base', '0003_auto_20181124_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('linked_stops', models.CharField(max_length=100)),
            ],
        ),
    ]
