class Player:
    def __init__(self, player_name, team):
        self.player_name = player_name
        self.team = team

    def display(self):
        print("Player Name:", self.player_name)
        print("Team:", self.team)

p1 = Player("Virat Kohli", "India")

p1.display()