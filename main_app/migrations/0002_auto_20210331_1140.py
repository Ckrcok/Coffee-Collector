# Generated by Django 3.1.7 on 2021-03-31 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.CreateModel(
            name='Sugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=8)),
                ('amout', models.IntegerField(max_length=1)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.coffee')),
            ],
        ),
    ]
