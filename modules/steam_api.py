import requests


class SteamAPI:
    URL = "https://store.steampowered.com/api/appdetails"

    def get_app(self, appid):
        response = requests.get(
            self.URL,
            params={
                "appids": appid,
                "cc": "br",
                "l": "brazilian"
            },
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return data.get(str(appid), {})

    def get_prices(self, appids):
        if isinstance(appids, list):
            appids = ",".join(str(i) for i in appids)

        response = requests.get(
            self.URL,
            params={
                "appids": appids,
                "cc": "br",
                "l": "brazilian",
                "filters": "price_overview"
            },
            timeout=20
        )

        response.raise_for_status()

        return response.json()
