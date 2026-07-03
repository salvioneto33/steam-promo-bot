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
                    "description": f"🔥 **{game['discount']}% OFF**\n💰 **US$ {game['price']}**",
                    "image": {
                        "url": game["image"]
                    },
                    "color": 3066993
                }
            ]
        }

        response = requests.post(self.webhook, json=payload, timeout=15)
        response.raise_for_status()
