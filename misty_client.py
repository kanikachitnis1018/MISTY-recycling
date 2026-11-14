# misty_client.py
from fileinput import filename
import os
import base64
import requests
from config import BASE_URL, CAPTURED_DIR

class MistyClient:
    def __init__(self):
        self.base_url = BASE_URL
        # Ensure the captured images directory exists locally
        os.makedirs(CAPTURED_DIR, exist_ok=True)

    def change_led(self, red: int, green: int, blue: int):
        url = f"{self.base_url}/led"
        payload = {"red": red, "green": green, "blue": blue}
        return requests.post(url, json=payload).json()

    def display_image(self, image_filename: str):
        url = f"{self.base_url}/images/display"
        payload = {"FileName": image_filename}
        return requests.post(url, json=payload).json()

    def speak(self, text: str, pitch: float = 1.1, speech_rate: float = 0.95):
        """Makes Misty speak. Slightly higher pitch & slower rate works great for kids."""
        url = f"{self.base_url}/tts/speak"
        payload = {
            "text": text,
            "pitch": pitch,
            "speechRate": speech_rate,
            "flush": True
        }
        return requests.post(url, json=payload).json()

    def take_and_download_picture(self, filename="captured_object.jpg") -> str:
        """Triggers Misty's RGB camera, downloads the image, and saves it locally."""
        url = f"{self.base_url}/cameras/rgb"
        params = {
            "fileName": filename,
            "base64": True,
            "overwriteExisting": True
        }
        
        try:
            print(f"Commanding Misty to snap a picture...")
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            # Extract base64 and save directly as a clean .jpg file
            base64_data = data["result"]["base64"]
            img_bytes = base64.b64decode(base64_data)
            
            save_path = os.path.join(CAPTURED_DIR, filename)
            with open(save_path, "wb") as f:
                f.write(img_bytes)
            
            print(f"Picture successfully saved to {save_path}!")
            return save_path
            
        except Exception as e:
            print(f"ERROR: Failed to capture picture from Misty: {e}")
            raise e