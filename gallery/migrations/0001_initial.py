# Generated by Django 3.2.4 on 2021-08-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('SF', 'sofa'), ('CH', 'chair'), ('BF', 'bed frames'), ('O', 'other')], default='O', max_length=2)),
                ('color', models.CharField(choices=[('R', 'red'), ('B', 'blue'), ('G', 'green')], default='R', max_length=2)),
                ('style', models.CharField(choices=[('MOD', 'modern'), ('VCT', 'victorian'), ('FAN', 'fancy'), ('SIM', 'simple')], default='SIM', max_length=3)),
                ('size', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
    ]
