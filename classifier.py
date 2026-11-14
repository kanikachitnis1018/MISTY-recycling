# classifier.py
import os
import cv2
import numpy as np
from config import REFERENCE_DIR
from categories import PHONE

class PhoneClassifier:
    def __init__(self):
        self.phone_histograms = []
        self.load_references()

    def load_references(self):
        """Loads all reference images for the phone and computes their color histograms."""
        phone_folder = os.path.join(REFERENCE_DIR, PHONE)
        
        if not os.path.exists(phone_folder):
            print(f"Warning: Reference folder '{phone_folder}' does not exist yet!")
            return
            
        for img_name in os.listdir(phone_folder):
            img_path = os.path.join(phone_folder, img_name)
            img = cv2.imread(img_path)
            if img is not None:
                hist = self._compute_histogram(img)
                self.phone_histograms.append(hist)
        
        print(f"Loaded {len(self.phone_histograms)} reference images for 'phone'.")

    def _compute_histogram(self, image):
        """Computes a normalized HSV color histogram for an image."""
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])
        cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        return hist

    def recognize_phone(self, captured_image_path: str, threshold: float = 0.5) -> bool:
        """Compares captured image histogram against phone references."""
        cap_img = cv2.imread(captured_image_path)
        if cap_img is None:
            raise ValueError(f"Could not read captured image at {captured_image_path}")
            
        cap_hist = self._compute_histogram(cap_img)
        
        if not self.phone_histograms:
            print("No reference histograms found!")
            return False

        scores = []
        for ref_hist in self.phone_histograms:
            # Compare using Correlation (1.0 = identical, 0.0 = completely different)
            score = cv2.compareHist(cap_hist, ref_hist, cv2.HISTCMP_CORREL)
            scores.append(score)
        
        avg_score = np.mean(scores)
        print(f"Match confidence score for phone: {avg_score:.2f}")
        
        # Return True if score is above the matching threshold
        return avg_score >= threshold