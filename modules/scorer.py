import math


class Scorer:

    def calculate(self, discount, price, reviews):

        score = 0

        # Desconto
        score += discount

        # Reviews
        if reviews > 0:
            score += math.log10(reviews) * 10

        # Preço (quanto menor, melhor)
        score += max(0, 100 - price)

        return round(score, 2)
