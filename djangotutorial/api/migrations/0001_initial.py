# Generated by Django 2.1.2 on 2018-10-14 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('victories', models.IntegerField(default=0)),
                ('defeats', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=12)),
                ('captain', models.BooleanField(default=False)),
                ('sled', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Sled')),
            ],
        ),
    ]
