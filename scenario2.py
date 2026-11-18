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

    speak("Let's look at it together.")
    time.sleep(4)

    speak("What do you think it's made of?")
    time.sleep(5)

    speak("That's right! Which bin do you think it belongs in?")
    time.sleep(6)

    speak("The paper bin.")
    time.sleep(4)

    speak("Yes! Great job!")