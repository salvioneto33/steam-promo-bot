from modules.cheapshark import CheapShark
from modules.steam_api import SteamAPI

cheapshark = CheapShark()
steam = SteamAPI()

deal = cheapshark.get_deals(limit=1)[0]

appid = deal["steamAppID"]

reviews = steam.get_reviews(appid)

print(reviews)
