class Game:

    def __init__(self, dto):
        self.id = dto["id"]
        self.team1 = dto["home_team"]
        self.team2 = dto["away_team"]
        self.status = "PENDING"
        self.winner = ""
        # bookmakers = dto["bookmakers"]
        # for bookmaker in bookmakers:
        #     if bookmaker.key == "barstool":
        #         self.book = bookmaker
        # for 

    def __str__(self):
        return str.format("{} {}", self.team1, self.team2)

    
