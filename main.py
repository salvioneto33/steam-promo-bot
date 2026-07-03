from modules.steam_service import SteamService
from modules.steam_api import SteamAPI
from modules.discord_webhook import DiscordWebhook

service = SteamService()
steam = SteamAPI()
discord = DiscordWebhook()

deal = service.get_deals(limit=1)[0]

appid = deal["steamAppID"]

app = steam.get_app(appid)

if not app.get("success"):
    raise Exception("Erro ao consultar a Steam")

data = app["data"]

prices = steam.get_prices([appid])

price = prices[str(appid)]["data"]["price_overview"]

game = {
    "name": data["name"],
    "image": data["header_image"],
    "old_price": price["initial_formatted"],
    "price": price["final_formatted"],
    "discount": price["discount_percent"],
    "url": f"https://store.steampowered.com/app/{appid}/"
}

discord.send_game(game)

print("Promoção enviada com sucesso!")
