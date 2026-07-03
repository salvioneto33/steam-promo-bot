import json
import os


class History:

    FILE = "history.json"

    def load(self):

        if not os.path.exists(self.FILE):
            return []

        with open(self.FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, history):

        with open(self.FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def exists(self, appid):

        return appid in self.load()

    def add(self, appid):

        history = self.load()

        if appid not in history:
            history.append(appid)

        self.save(history)
