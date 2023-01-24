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
    link = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"Название: {self.name}, размер: {self.size}"

    class Meta:
        verbose_name = 'Свеча'
        verbose_name_plural = 'Свечи'


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
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'Название: {self.name}'

    class Meta:
        verbose_name = 'Чашка'
        verbose_name_plural = 'Чашки'


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
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'Название: {self.name}'

    class Meta:
        verbose_name = 'Мыло'
        verbose_name_plural = 'Мыло'
