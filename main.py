from modules.steam_service import SteamService

service = SteamService()

deals = service.get_deals()

print(f"Foram encontradas {len(deals)} promoções.\n")

for game in deals[:10]:
    print(
        f"{game['title']}\n"
        f"Steam AppID: {game.get('steamAppID')}\n"
        f"Preço: {game['salePrice']}\n"
        f"Desconto: {game['savings'][:5]}%\n"
    )
