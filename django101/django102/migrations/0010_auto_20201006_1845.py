# Generated by Django 3.1.2 on 2020-10-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0009_auto_20201006_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='level_of_difficulty',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], default='ME', max_length=2),
        ),
    ]
