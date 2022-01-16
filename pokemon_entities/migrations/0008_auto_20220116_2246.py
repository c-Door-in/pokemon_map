# Generated by Django 3.1.14 on 2022-01-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20220116_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(upload_to='pokemons'),
        ),
    ]