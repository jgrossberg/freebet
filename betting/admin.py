from django.contrib import admin

from .models import Bet, Bettor, Game


class BetAdmin(admin.ModelAdmin):
    fields = ['bettor', 'game', 'amount']
    
class BettorAdmin(admin.ModelAdmin):
    fields = ['user', 'balance']
    
class GameAdmin(admin.ModelAdmin):
    fields = ['team1', 'team2', 'winner']
    
admin.site.register(Bet, BetAdmin)
admin.site.register(Bettor, BettorAdmin)
admin.site.register(Game, GameAdmin)