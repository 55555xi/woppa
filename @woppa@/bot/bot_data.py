# bot_data.py
class BotData:
    def __init__(self, woppa_hotkey, exit_hotkey, random_woppa, base_woppa, tolerance, threshold, woppa_lower, woppa_upper):
        self.woppa_hotkey = woppa_hotkey
        self.exit_hotkey = exit_hotkey
        self.random_woppa = random_woppa
        self.base_delay = base_woppa
        self.tolerance = tolerance
        self.threshold = threshold
        self.woppa_lower = woppa_lower
        self.woppa_upper = woppa_upper