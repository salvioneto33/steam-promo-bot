from modules.steam_service import SteamService
from modules.steam_api import SteamAPI

service = SteamService()
steam = SteamAPI()

deal = service.get_deals(limit=1)[0]

appid = deal["steamAppID"]

prices = steam.get_prices([appid])

price = prices[str(appid)]["data"]["price_overview"]

print(f"Nome: {deal['title']}")
print(f"Preço original: {price['initial_formatted']}")
print(f"Preço atual: {price['final_formatted']}")
print(f"Desconto: {price['discount_percent']}%")
print(f"Link: https://store.steampowered.com/app/{appid}/")
