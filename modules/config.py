import json


class Config:

    def __init__(self):
        with open("config.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)

    @property
    def max_games(self):
        return self.data["max_games"]

    @property
    def min_discount(self):
        return self.data["min_discount"]

    @property
    def max_price(self):
        return self.data["max_price"]

    @property
    def min_reviews(self):
        return self.data["min_reviews"]
