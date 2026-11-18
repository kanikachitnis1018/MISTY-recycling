import requests
import time

# Misty's IP address
ROBOT_IP = "172.20.10.12"
BASE_URL = f"http://{ROBOT_IP}/api"


def speak(text):
    payload = {
        "Text": text,
        "Flush": True
    }

    try:
        response = requests.post(
            f"{BASE_URL}/tts/speak",
            json=payload,
            timeout=15
        )

        print(f"Misty says: {text}")
        print("Status:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Speech command failed:", e)


if __name__ == "__main__":

    speak("I know this is recyclable, but which bin is it?")
    time.sleep(6)

    speak("We know it's plastic. Can you see which bin might take plastic?")
    time.sleep(7)

    speak("Yes! The glass, metal, plastic bin.")
    time.sleep(5)

    speak("That's the one! Great job!")