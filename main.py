from modules.steam_service import SteamService
from modules.steam_api import SteamAPI

service = SteamService()
steam = SteamAPI()

deal = service.get_deals(limit=1)[0]

appid = deal["steamAppID"]

app = steam.get_app(appid)

if not app.get("success"):
    raise Exception("Erro ao consultar Steam")

data = app["data"]

print(f"Nome: {data['name']}")
print(f"AppID: {appid}")
print(f"Imagem: {data['header_image']}")
print(f"Preço: ${deal['salePrice']}")
print(f"Desconto: {round(float(deal['savings']))}%")
print(f"Link: https://store.steampowered.com/app/{appid}/")
