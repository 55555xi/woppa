# woppabot.py
from bot.bot_data import BotData
from bot.bot_actions import BotActions
from bot.bot_data_loader import BotDataLoader
from utils.utils import Utils
class WoppaBot:
    def __init__(self):
        print("Wireshark...")
        bot_data_loader = BotDataLoader()
        try:
            bot_data = bot_data_loader.load_bot_data()
        except Exception:
            Utils.exiting()
        self.bot_actions = BotActions(bot_data)
        print("Ready Wireshark")
    def starter(self):
        self.bot_actions.starter()