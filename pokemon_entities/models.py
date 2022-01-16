from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons', blank=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.title_ru)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()

    def __str__(self):
        return '{} at lat: {}, lon: {}'.format(
            self.pokemon,
            self.lat,
            self.lon,
        )
