class CricketPlayer:
    def __init__(self, player_name, runs, matches):
        self.player_name = player_name
        self.runs = runs
        self.matches = matches

    def display(self):
        print("Player Name:", self.player_name)
        print("Runs:", self.runs)
        print("Matches:", self.matches)

p1 = CricketPlayer("Virat Kohli", 13848, 295)

p1.display()