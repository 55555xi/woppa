# delay_manager.py
import numpy as np
import time
from time import sleep
class DelayManager:
    def __init__(self, base_woppa, random_woppa):
        self.base_delay = base_woppa
        self.random_woppa = random_woppa
        self.rng = np.random.default_rng()    
    def make_shoot_delay(self):
        delay_percentage = self.random_woppa / 100.0 * self.rng.random()
        actual_delay = self.base_delay + self.base_delay * delay_percentage
        time.sleep(actual_delay)
    def make_check_delay(self):
        time.sleep(0.1)