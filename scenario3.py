import requests
import time

ROBOT_IP = "192.168.0.248"
BASE_URL = f"http://{ROBOT_IP}/api"

# ============================================================
# TIMING
# ============================================================

START_PAUSE = 0
CHILD_START_PAUSE = 2
CHILD_RESPONSE_PAUSE = 10
DISPOSAL_PAUSE = 3
SHORT_PAUSE = 2
END_PAUSE = 3

# ============================================================
# COLOURS / EXPRESSIONS
# ============================================================

BLUE = (0, 100, 255)
GREEN = (0, 255, 0)

DEFAULT_FACE = "e_DefaultContent.jpg"
ADMIRE_FACE = "e_Admiration.jpg"


# ============================================================
# SPEECH
# ============================================================

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
        print("Speech:", response.status_code, response.text)

    except requests.exceptions.RequestException as e:
        print("SPEECH FAILED:", e)


# ============================================================
# LED
# ============================================================

def set_colour(colour):
    r, g, b = colour

    payload = {
        "Red": r,
        "Green": g,
        "Blue": b
    }

    try:
        response = requests.post(
            f"{BASE_URL}/led",
            json=payload,
            timeout=10
        )

        print(
            f"LED RGB({r},{g},{b}):",
            response.status_code,
            response.text
        )

    except requests.exceptions.RequestException as e:
        print("LED FAILED:", e)


# ============================================================
# FACE
# ============================================================

def show_face(filename):
    payload = {
        "FileName": filename,
        "Alpha": 1
    }

    try:
        response = requests.post(
            f"{BASE_URL}/images/display",
            json=payload,
            timeout=10
        )

        print(
            f"FACE {filename}:",
            response.status_code,
            response.text
        )

    except requests.exceptions.RequestException as e:
        print("FACE FAILED:", e)


# ============================================================
# ARMS
# ============================================================

def move_arms(left, right, velocity=60):
    payload = {
        "LeftArmPosition": left,
        "RightArmPosition": right,
        "LeftArmVelocity": velocity,
        "RightArmVelocity": velocity,
        "Units": "degrees"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/arms/set",
            json=payload,
            timeout=10
        )

        print(
            f"ARMS L={left} R={right}:",
            response.status_code,
            response.text
        )

    except requests.exceptions.RequestException as e:
        print("ARMS FAILED:", e)


# ============================================================
# HEAD
# ============================================================

def move_head(pitch, roll, yaw, velocity=100):
    payload = {
        "Pitch": pitch,
        "Roll": roll,
        "Yaw": yaw,
        "Velocity": velocity,
        "Units": "degrees"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/head",
            json=payload,
            timeout=10
        )

        print(
            f"HEAD P={pitch} R={roll} Y={yaw}:",
            response.status_code,
            response.text
        )

    except requests.exceptions.RequestException as e:
        print("HEAD FAILED:", e)


# ============================================================
# FULL RESET
# ============================================================

def reset_body():
    print("\n--- FULL RESET ---")

    # Both arms completely down
    move_arms(
        left=90,
        right=90,
        velocity=100
    )

    # Head centred
    move_head(
        pitch=0,
        roll=0,
        yaw=0,
        velocity=100
    )

    # Default face
    show_face(DEFAULT_FACE)

    # Blue listening light
    set_colour(BLUE)

    # Give physical reset time to finish
    time.sleep(2)


# ============================================================
# ADMIRE
# ============================================================

def admire():
    print("\n--- ADMIRE ---")

    # Admiration expression
    show_face(ADMIRE_FACE)

    # Admire head pose
    move_head(
        pitch=-5,
        roll=0,
        yaw=0,
        velocity=100
    )

    # Admire arm pose
    move_arms(
        left=-89,
        right=89,
        velocity=50
    )

    # Pure green = correct
    set_colour(GREEN)

    time.sleep(2)


# ============================================================
# LOOK AT GLASS / METAL / PLASTIC BIN
#
# Bin assumed to be on Binnie's RIGHT.
# Negative yaw = right.
# ============================================================

def look_at_plastic_bin():
    print("\n--- LOOKING AT GLASS/METAL/PLASTIC BIN ---")

    move_head(
        pitch=18,       # Look down
        roll=0,
        yaw=-30,        # Turn RIGHT
        velocity=95
    )

    # Hold gaze
    time.sleep(1.5)


# ============================================================
# HEAD BACK TO CENTRE
# ============================================================

def centre_head():
    print("\n--- HEAD BACK TO CENTRE ---")

    move_head(
        pitch=0,
        roll=0,
        yaw=0,
        velocity=100
    )

    time.sleep(1)


# ============================================================
# FINAL CELEBRATION
# BOTH arms up + disco lights
# ============================================================

def celebrate():
    print("\n--- CELEBRATION ---")

    celebration_colours = [
        (255, 165, 0),     # Orange
        (255, 255, 0),     # Yellow
        (0, 255, 0),       # Green
        (0, 100, 255),     # Blue
        (255, 0, 255),     # Pink
        (0, 255, 255),     # Cyan
    ]

    # BOTH arms up together
    move_arms(
        left=-29,
        right=-29,
        velocity=100
    )

    time.sleep(0.5)

    # Disco lights
    for _ in range(3):
        for colour in celebration_colours:
            set_colour(colour)
            time.sleep(0.2)

    # Hold both arms up
    time.sleep(1.5)


# ============================================================
# SCENARIO 3 - PARTIAL UNDERSTANDING
# PLASTIC WRAPPER
# ============================================================

if __name__ == "__main__":

    print("\n==============================")
    print("BINNIE - SCENARIO 3")
    print("PARTIAL UNDERSTANDING")
    print("PLASTIC WRAPPER")
    print("==============================")


    # ========================================================
    # STANDARD START
    #
    # Arms down
    # Head centre
    # Default face
    # Blue light
    # ========================================================

    reset_body()

    time.sleep(START_PAUSE)


    # ========================================================
    # CHILD STARTS THE INTERACTION
    #
    # CHILD SAYS:
    #
    # "I know this is recyclable,
    #  but I don't know which bin it goes in."
    #
    # ========================================================

    print(
        "CHILD: I know this is recyclable, "
        "but I don't know which bin it goes in."
    )

    time.sleep(CHILD_START_PAUSE)


    # ========================================================
    # BINNIE ACKNOWLEDGES EXISTING UNDERSTANDING
    # ========================================================

    speak("You're right, it can be recycled!")

    time.sleep(SHORT_PAUSE)


    # ========================================================
    # REMIND CHILD OF MATERIAL
    # ========================================================

    speak("Remember, the wrapper is made of plastic.")

    time.sleep(SHORT_PAUSE)


    # ========================================================
    # GUIDE CHILD TOWARDS CORRECT BIN
    # ========================================================

    speak(
        "Can you find the recycling bin "
        "that takes plastic?"
    )

    # CHILD LOOKS AT THE BINS AND ANSWERS
    time.sleep(CHILD_RESPONSE_PAUSE)


    # ========================================================
    # CHILD GETS IT RIGHT
    #
    # Admire + green
    # ========================================================

    admire()

    speak("Yes! That’s correct!")

    time.sleep(SHORT_PAUSE)


    # ========================================================
    # LOOK TOWARDS GLASS / METAL / PLASTIC BIN
    #
    # Right + down
    # ========================================================

    look_at_plastic_bin()


    # ========================================================
    # CHILD PHYSICALLY DISPOSES OF PLASTIC WRAPPER
    # ========================================================

    time.sleep(DISPOSAL_PAUSE)


    # ========================================================
    # HEAD BACK TO CENTRE
    # ========================================================

    centre_head()

    time.sleep(0.5)


    # ========================================================
    # FINAL DIALOGUE
    # ========================================================

    speak("Great job figuring that out!")

    time.sleep(0.8)


    # ========================================================
    # FINAL CELEBRATION
    #
    # Both arms up + disco lights
    # ========================================================

    celebrate()

    time.sleep(END_PAUSE)


    # ========================================================
    # FULL RESET
    # ========================================================

    reset_body()

    print("\nScenario 3 complete.")