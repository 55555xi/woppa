# bot_data_loader.py
import json
from bot.bot_data import BotData
class BotDataLoader:
    def __init__(self, config_path='resourses/config.json'):
        self.config_path = config_path
    def load_bot_data(self):
        with open(self.config_path) as jsonFile:
            data = json.load(jsonFile)
        try:
            bot_data = BotData(
                woppa_hotkey=int(data["woppa_hotkey"], 16),
                exit_hotkey=int(data["exit_hotkey"], 16),
                random_woppa=data["random_woppa"],
                base_woppa=data["base_woppa"],
                tolerance=data["tolerance"],
                threshold=data["threshold"],
                woppa_lower=data["woppa_lower"],
                woppa_upper=data["woppa_upper"]
            )
            return bot_data
        except KeyError as e:
            print(f"Configuration key error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise
