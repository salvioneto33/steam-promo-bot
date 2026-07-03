import requests


class SteamService:
    URL = "https://www.cheapshark.com/api/1.0/deals"

    def get_deals(self, limit=20):
        params = {
            "storeID": 1,      # Steam
            "pageSize": limit,
            "sortBy": "Savings"
        }

        response = requests.get(self.URL, params=params, timeout=15)
        response.raise_for_status()

        return response.json()
