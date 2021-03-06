# Generated by Django 2.1.7 on 2019-04-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=3, verbose_name='Country Code')),
                ('value', models.IntegerField(default=0, verbose_name='Colour Intensity')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkMapConnections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1, verbose_name='Connection Strength')),
            ],
            options={
                'ordering': ['-source'],
            },
        ),
        migrations.CreateModel(
            name='NetworkMapNodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField(unique=True, verbose_name='Node ID')),
                ('name', models.CharField(max_length=100, verbose_name='Node Name')),
                ('value', models.IntegerField(default=1, verbose_name='Size of Node')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='networkmapconnections',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='visualisation.NetworkMapNodes', verbose_name='Source Node ID'),
        ),
        migrations.AddField(
            model_name='networkmapconnections',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='visualisation.NetworkMapNodes', verbose_name='Target Node ID'),
        ),
    ]
