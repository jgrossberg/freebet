from django.db import models
from django.contrib.auth.models import User

class Bettor(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = False, null = False)
    balance = models.DecimalField(decimal_places=4, max_digits=32)

    def __str__(self):
        return str.format("{}:{}", self.user, self.balance)

class Team(models.Model):
    city = models.TextField()
    name = models.TextField()
    sport = models.TextField()

    def __str__(self):
        return str.format(self.city)

class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name="team_1", on_delete=models.DO_NOTHING, blank=False, null=False)
    team2 = models.ForeignKey(Team, related_name="team_2", on_delete=models.DO_NOTHING, blank=False, null=False)
    status = models.TextField()
    winner = models.TextField()

    def __str__(self):
        return str.format("{} vs {}", self.team1, self.team2)


class Line(models.Model):
    OVER_UNDER_CHOICES = [("OVER", "over"), ("UNDER", "under")]
    TYPE_CHOICES = [("TOTAL", "Total"), ("ML", "Moneyline"), ("SPREAD", "Spread")]

    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.PROTECT, blank=False, null=False)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, blank=True, null=True)
    points = models.DecimalField(decimal_places=2, max_digits=4)
    odds = models.DecimalField(decimal_places=0, max_digits=5)
    side = models.CharField(max_length=10, choices=OVER_UNDER_CHOICES, blank=True)

    def __str__(self):
        return str.format("{} {}{} {}", self.type, self.side, self.points, self.odds)


class Bet(models.Model):
    bettor = models.ForeignKey(Bettor, on_delete = models.DO_NOTHING, blank = False, null = False)
    game = models.ForeignKey(Game, on_delete=models.PROTECT, blank=False, null=False)
    line = models.ForeignKey(Line, on_delete=models.PROTECT, blank=False, null=False)
    amount = models.DecimalField(decimal_places=4, max_digits=16)
    odds = models.IntegerField()

    def __str__(self):
        return str.format("{} - {}: {}", self.bettor, self.amount, self.game)


