from modules.cheapshark import CheapShark


class SteamService:

    def __init__(self):
        self.cheapshark = CheapShark()

    def get_deals(self, limit=20):
        return self.cheapshark.get_deals(limit)
