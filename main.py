from modules.steam_service import SteamService

service = SteamService()

deals = service.get_deals()

print(f"Foram encontradas {len(deals)} promoções.\n")

for game in deals[:10]:
    print(
        f"{game['title']} | "
        f"{game['salePrice']} | "
        f"{game['savings'][:5]}%"
    )
