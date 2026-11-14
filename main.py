# main.py
import time
from misty_client import MistyClient
from dialogue import DialogueEngine
from classifier import PhoneClassifier

def test_greeting():
    print("Initializing Misty client...")
    misty = MistyClient()

    print("Setting blue LED and neutral face...")
    misty.change_led(0, 0, 255)  # Blue LED for waiting/ready state
    misty.display_image("e_DefaultContent.jpg")

    print("Making Misty speak the greeting...")
    greeting_text = DialogueEngine.get_greeting()
    print(f"Misty says: '{greeting_text}'")
    
    # Send the speech command
    misty.speak(greeting_text)
    print("Greeting command sent successfully!")


def test_phone_recognition():
    print("Initializing Misty and Classifier...")
    misty = MistyClient()
    classifier = PhoneClassifier()

    # 1. Ready state
    misty.change_led(0, 0, 255)  # Blue LED
    misty.display_image("e_DefaultContent.jpg")
    misty.speak("Hold up your phone in front of my camera!")
    
    print("Waiting 4 seconds for you to hold up the phone...")
    time.sleep(4)

    # 2. Capture photo from Misty's camera
    print("Taking picture...")
    image_path = misty.take_and_download_picture("test_phone.jpg")

    # 3. Classify / Recognize
    is_phone = classifier.recognize_phone(image_path, threshold=0.25)

    # 4. React based on result
    if is_phone:
        print("Result: It's a phone!")
        misty.change_led(0, 255, 0)  # Green LED
        misty.display_image("e_Joy.jpg")
        misty.speak("I see your phone! Great job.")
    else:
        print("Result: Not recognized as a phone.")
        misty.change_led(255, 0, 0)  # Red LED
        misty.display_image("e_ApprehensionConcerned.jpg")
        misty.speak("Hmm, I don't see a phone. Try holding it closer!")


if __name__ == "__main__":
    # Run the greeting first
    test_greeting()
    time.sleep(4) # Pause briefly between tests
    
    # Then run the phone recognition test
    test_phone_recognition()