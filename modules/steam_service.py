from modules.cheapshark import CheapShark
from modules.steam_api import SteamAPI
from modules.config import Config
from modules.scorer import Scorer


class SteamService:

    def __init__(self):
        self.cheapshark = CheapShark()
        self.steam = SteamAPI()
        self.config = Config()
        self.scorer = Scorer()

    def get_best_deals(self):

        games = []

        deals = self.cheapshark.get_deals(limit=200)

        for deal in deals:

            appid = deal.get("steamAppID")

            if not appid:
                continue

            try:

                app = self.steam.get_app(appid)

                if not app.get("success"):
                    continue

                data = app["data"]

                prices = self.steam.get_prices([appid])

                if (
                    str(appid) not in prices
                    or "price_overview" not in prices[str(appid)]["data"]
                ):
                    continue

                price = prices[str(appid)]["data"]["price_overview"]

                if price["discount_percent"] < self.config.min_discount:
                    continue

                price_brl = price["final"] / 100

                if price_brl > self.config.max_price:
                    continue

                reviews = self.steam.get_reviews(appid)

                total_reviews = reviews["query_summary"].get("total_reviews", 0)

                if total_reviews < self.config.min_reviews:
                    continue

                score = self.scorer.calculate(
                    discount=price["discount_percent"],
                    price=price_brl,
                    reviews=total_reviews
                )

                games.append({
                    "name": data["name"],
                    "image": data["header_image"],
                    "old_price": price["initial_formatted"],
                    "price": price["final_formatted"],
                    "discount": price["discount_percent"],
                    "reviews": total_reviews,
                    "score": score,
                    "url": f"https://store.steampowered.com/app/{appid}/"
                })

            except Exception:
                continue

        games.sort(key=lambda x: x["score"], reverse=True)

        return games[:self.config.max_games]
