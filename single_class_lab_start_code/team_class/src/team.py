class Team:
    def __init__(self, name, players, coach):
        self.name = name 
        self.players = players
        self.coach = coach 
        self.points = 0

    def add_player(self, player):
        self.players.append(player)
    
    def has_player(self, check_player):
        for player in self.players:
            if player == check_player:
                return True
        else:
            return False
        
    def play_game(self, won):
        if won == True:
            self.points += 3
    