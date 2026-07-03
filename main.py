from modules.steam_api import buscar_promocoes

print("Buscando promoções...\n")

jogos = buscar_promocoes()

for jogo in jogos:
    print(jogo["nome"])
    print(f'Desconto: {jogo["desconto"]}%')
    print(f'Preço: R$ {jogo["preco_final"]:.2f}')
    print("-" * 40)
