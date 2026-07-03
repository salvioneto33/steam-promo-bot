import requests

STEAM_FEATURED_URL = "https://store.steampowered.com/api/featured"


def buscar_promocoes():
    resposta = requests.get(
        STEAM_FEATURED_URL,
        params={
            "cc": "br",
            "l": "portuguese"
        },
        timeout=15
    )

    resposta.raise_for_status()

    dados = resposta.json()

    especiais = dados.get("specials", {}).get("items", [])

    jogos = []

    for jogo in especiais:
        jogos.append({
            "appid": jogo["id"],
            "nome": jogo["name"],
            "desconto": jogo["discount_percent"],
            "preco_original": jogo["original_price"] / 100,
            "preco_final": jogo["final_price"] / 100,
            "imagem": jogo["large_capsule_image"]
        })

    return jogos
