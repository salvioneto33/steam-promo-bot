from modules.cheapshark import CheapShark
from modules.steam_api import SteamAPI


class SteamService:

    def __init__(self):
        self.cheapshark = CheapShark()
        self.steam = SteamAPI()

    def get_best_deals(self, limit=5):

        games = []

        deals = self.cheapshark.get_deals(limit=limit)

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

                games.append({
                    "name": data["name"],
                    "image": data["header_image"],
                    "old_price": price["initial_formatted"],
                    "price": price["final_formatted"],
                    "discount": price["discount_percent"],
                    "url": f"https://store.steampowered.com/app/{appid}/"
                })

            except Exception:
                continue

        return games
