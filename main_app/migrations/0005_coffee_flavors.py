# Generated by Django 3.1.7 on 2021-04-02 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210331_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='flavors',
            field=models.ManyToManyField(to='main_app.Flavor'),
        ),
    ]
