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
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        return data.get(str(appid), {})
