from modules.steam_service import SteamService
from modules.discord_webhook import DiscordWebhook

service = SteamService()
discord = DiscordWebhook()

games = service.get_best_deals()

if not games:
    print("Nenhuma promoção encontrada com os filtros atuais.")
else:
    for game in games:
        discord.send_game(game)

    print(f"{len(games)} promoções enviadas com sucesso!")
