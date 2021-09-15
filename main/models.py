from django.db import models
from decimal import Decimal


class Player(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя игрока")
    email = models.EmailField(verbose_name="Почта игрока")
    is_sponsor = models.BooleanField(default=False, verbose_name="Огранизатор?")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Game(models.Model):
    sponsor = models.ForeignKey(Player, on_delete=models.CASCADE)
    price = models.DecimalField(blank=True, max_digits=7, decimal_places=2, default=Decimal('00000.00'))
    is_price_limit = models.BooleanField(default=False,
                                         verbose_name="Ограничиваем цену подарка?")
    # Если True - подарки желательно ограничивать пределом price
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.sponsor} ({self.start_date})"

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Wish(models.Model):
    declaration = models.TextField(max_length=200, verbose_name="Описание желаемого подарка")
    wisher = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='wish_wisher')
    selected = models.BooleanField(default=False,
                                   verbose_name="Подарок выбран?")  # Если True - этот подарок уже кто-то выбрал дарить

    def __str__(self):
        return self.declaration

    class Meta:
        verbose_name = 'Желанный подарок'
        verbose_name_plural = 'Желанные порарки'


class Hate(models.Model):
    hater = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, related_name='hate_hater')
    declaration = models.TextField(max_length=200, verbose_name="Описание НЕжелательного подарка")

    def __str__(self):
        return self.declaration

    class Meta:
        verbose_name = 'НЕжеланный подарок'
        verbose_name_plural = 'Нежеланные порарки'


# внутренняя таблица связи "Дарящий-Подарок"
class WishGrantor(models.Model):
    grantor = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, related_name='grantor_wish')
    wish = models.ForeignKey(Wish, on_delete=models.RESTRICT, blank=True, related_name='wish_grantor')
