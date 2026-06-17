
class Movie:
    def __init__(self, movie_name, hero, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.rating = rating

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Hero:", self.hero)
        print("Rating:", self.rating)

movie1 = Movie("Jawan", "Shah Rukh Khan", 8.0)

movie1.display()