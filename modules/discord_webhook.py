import os
import requests


class DiscordWebhook:

    def __init__(self):
        self.webhook = os.environ["DISCORD_WEBHOOK"]

    def send_game(self, game):

        payload = {
            "embeds": [
                {
                    "title": game["name"],
                    "url": game["url"],
                    "description":
                        f"~~{game['old_price']}~~\n\n"
                        f"## 💰 {game['price']}\n\n"
                        f"🔥 **{game['discount']}% OFF**",
                    "image": {
                        "url": game["image"]
                    },
                    "color": 5763719,
                    "footer": {
                        "text": "Steam Promo BR 🇧🇷"
                    }
                }
            ]
        }

        response = requests.post(self.webhook, json=payload, timeout=15)
        response.raise_for_status()
