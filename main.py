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
    raise Exception("Erro ao consultar Steam")

data = app["data"]

game = {
    "name": data["name"],
    "image": data["header_image"],
    "price": deal["salePrice"],
    "discount": round(float(deal["savings"])),
    "url": f"https://store.steampowered.com/app/{appid}/"
}

discord.send_game(game)

print("Promoção enviada para o Discord com sucesso!")
