# Generated by Django 3.1.14 on 2022-01-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20220117_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(null=True, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(null=True, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(null=True, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(null=True, verbose_name='Сила'),
        ),
    ]
