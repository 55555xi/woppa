# bot_actions.py
from utils.screen_capture import ScreenCapture
from utils.image_processing import ImageProcessor
from utils.utils import Utils
from bot.bot_controller import BotController
from bot.bot_data import BotData
from utils.delay_manager import DelayManager
class BotActions:
    def __init__(self, data: BotData):
        self.data = data
        self.woppabot = False
        self.exit_program = False
        self.bot_controller = BotController(data.woppa_hotkey, data.exit_hotkey)
        self.screen_capture = ScreenCapture()
        self.image_processor = ImageProcessor(data.tolerance, data.threshold, data.woppa_lower, data.woppa_upper)
        self.delay_manager = DelayManager(data.base_delay, data.random_woppa)     
    def searcher_in_o(self):
        img = self.screen_capture.capture()
        is_found = self.image_processor.process(img)
        if self.woppabot and is_found:
            self.delay_manager.make_shoot_delay()
            self.bot_controller.shoot()
    def hold(self):
        while True:
            if self.bot_controller.is_woppa_hotkey_pressed():
                self.woppabot = True
                self.searcher_in_o()
            else:
                self.delay_manager.make_check_delay()
            if self.bot_controller.is_exit_hotkey_pressed():
                print("Wireshark hold mode exit")
                self.exit_program = True
                Utils.exiting()
    def starter(self):
        while not self.exit_program:
            self.hold()
