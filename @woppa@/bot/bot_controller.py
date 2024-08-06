# bot_controller.py
import win32api
import keyboard
class BotController:
    def __init__(self, woppa_hotkey, exit_hotkey):
        self.woppa_hotkey = woppa_hotkey
        self.exit_hotkey = exit_hotkey
    def is_woppa_hotkey_pressed(self):
        return win32api.GetAsyncKeyState(self.woppa_hotkey) < 0
    def is_exit_hotkey_pressed(self):
        return win32api.GetAsyncKeyState(self.exit_hotkey) < 0 
    def shoot(self):
        print("Wireshark/Discord:821.")
        keyboard.press_and_release("ñ")