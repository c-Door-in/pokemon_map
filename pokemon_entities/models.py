from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Название (рус)', max_length=200)
    title_en = models.CharField('Название (анг)', max_length=200, blank=True)
    title_jp = models.CharField('Название (яп)', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='pokemons')
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        related_name='next_evolution',
        verbose_name='Предыдущая эволюция',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{} - {}'.format(self.id, self.title_ru)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entity',
        verbose_name='Покемон',
    )
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появился', null=True, blank=True)
    disappeared_at = models.DateTimeField('Исчез', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)

    def __str__(self):
        return '{} at lat: {}, lon: {}'.format(
            self.pokemon,
            self.lat,
            self.lon,
        )
