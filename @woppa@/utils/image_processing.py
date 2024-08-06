# image_processing.py
import numpy as np
import cv2
class ImageProcessor:
    def __init__(self, tolerance, threshold, woppa_lower, woppa_upper):
        self.tolerance = tolerance
        self.threshold = threshold
        self.woppa_lower = np.array(woppa_lower, dtype=np.uint8)
        self.woppa_upper = np.array(woppa_upper, dtype=np.uint8)
    def process(self, img):
        img_array = np.array(img)
        img_hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)        
        mask = cv2.inRange(img_hsv, self.woppa_lower, self.woppa_upper)      
        matching_pixels = np.sum(mask > 0)       
        return matching_pixels > self.threshold
