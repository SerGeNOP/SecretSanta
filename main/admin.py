from django.contrib import admin

from .models import Player, Game, Wish, Hate


@admin.register(Player)
class Player(admin.ModelAdmin):
    pass

    list_display = ('name', 'email', 'is_sponsor')


@admin.register(Game)
class Game(admin.ModelAdmin):
    pass

    list_display = ('sponsor', 'price', 'is_price_limit')


@admin.register(Wish)
class Wish(admin.ModelAdmin):
    pass

    list_display = ('wisher', 'declaration', 'selected')


@admin.register(Hate)
class Hate(admin.ModelAdmin):
    pass

    verbose_name = "Нежелательные подарки 10"
    list_display = ('hater', 'declaration')


