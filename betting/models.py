from django.db import models
from django.contrib.auth.models import User

class Bettor(models.Model):
    balance = models.DecimalField(decimal_places=4, max_digits=32)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = False, null = False)

class Game(models.Model):
    team1 = models.TextField()
    team2 = models.TextField()
    status = models.TextField()
    winner = models.TextField()

class Bet(models.Model):
    bettor = models.ForeignKey(Bettor, on_delete = models.DO_NOTHING, blank = False, null = False)
    game = models.ForeignKey(Game, on_delete=models.PROTECT, blank=False, null=False)
    amount = models.DecimalField(decimal_places=4, max_digits=16)

