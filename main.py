from modules.steam_service import SteamService
from modules.steam_api import SteamAPI

service = SteamService()
steam = SteamAPI()

deal = service.get_deals(limit=1)[0]

appid = deal["steamAppID"]

print(f"Buscando AppID {appid}...")

app = steam.get_app(appid)

print(app)
