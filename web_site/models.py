from django.db import models

smells = (
    ('клубника', 'клубника'),
    ('лаванда', 'лаванда'),
    ('апельсин', 'апельсин'),
    ('имбирное печенье', 'имбирное печенье')
)


class Candles(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveIntegerField()
    smell = models.CharField(choices=smells, max_length=50)
    wicks = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Название: {self.name}, размер: {self.size}"


colors = (
    ('розовый', 'розовый'),
    ('фиолетовый', 'фиолетовый'),
    ('бежевый', 'бежевый'),
    ('оранжевый', 'оранжевый')
)

materials = (
    ('стекло', 'стекло'),
    ('керамика', 'керамика'),
    ('пластик', 'пластик')
)


class Cups(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveIntegerField()
    color = models.CharField(choices=colors, max_length=50)
    material = models.CharField(choices=materials, max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'Название: {self.name}'


soap_colors = (
    ('жёлтый', 'жёлтый'),
    ('фиолетовый', 'фиолетовый'),
    ('голубой', 'голубой'),
    ('зелёный', 'зелёный'),
    ('красный', 'красный')
)


class Soap(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveIntegerField()
    color = models.CharField(choices=soap_colors, max_length=50)
    smell = models.CharField(choices=smells, max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'Название: {self.name}'
