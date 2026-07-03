import os
import requests

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

payload = {
    "content": "🚀 Steam Promo BR iniciado com sucesso!"
}

requests.post(WEBHOOK, json=payload, timeout=10)

print("Mensagem enviada com sucesso!")
