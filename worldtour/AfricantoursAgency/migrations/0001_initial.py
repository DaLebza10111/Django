# Generated by Django 5.0.7 on 2024-07-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_of_origin', models.CharField(max_length=64)),
                ('country_of_destination', models.CharField(max_length=64)),
                ('number_of_nights', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
