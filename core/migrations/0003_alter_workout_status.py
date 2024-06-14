# Generated by Django 5.0.6 on 2024-06-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='status',
            field=models.CharField(choices=[('Started', 'Started'), ('Finished', 'Finished')], default='Started', max_length=8),
        ),
    ]
