from django.contrib import admin

from .models import Bet, Bettor, Game, Line, Team


class BetAdmin(admin.ModelAdmin):
    fields = ['bettor', 'game', 'line', 'odds', 'amount']
    
class BettorAdmin(admin.ModelAdmin):
    fields = ['user', 'balance']
    
class GameAdmin(admin.ModelAdmin):
    fields = ['team1', 'team2', 'winner']
    
class LineAdmin(admin.ModelAdmin):
    fields = ['type', 'game', 'team', 'points', 'odds', 'side']

class TeamAdmin(admin.ModelAdmin):
    fields = ['city', 'name', 'sport']

admin.site.register(Bet, BetAdmin)
admin.site.register(Bettor, BettorAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Team, TeamAdmin)