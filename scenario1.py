import requests
import time

# ============================================================
# BINNIE - SCENARIO 1: CORRECT DECISION
# ============================================================

ROBOT_IP = "192.168.0.248"
BASE_URL = f"http://{ROBOT_IP}/api"

# ============================================================
# ADJUSTABLE PAUSES
# ============================================================

START_PAUSE = 2
CHILD_RESPONSE_PAUSE = 4
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
# Positive yaw = LEFT
# Positive pitch = DOWN
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
# STANDARD RESET
# ============================================================

def reset_body():
    print("\n--- RESET ---")

    # Arms down
    move_arms(
        left=90,
        right=90,
        velocity=40
    )

    # Head centred
    move_head(
        pitch=0,
        roll=0,
        yaw=0,
        velocity=100
    )

    # Default expression
    show_face(DEFAULT_FACE)

    # Blue listening light
    set_colour(BLUE)

    time.sleep(1)


# ============================================================
# ADMIRE
#
# Based on Binnie's actual installed Admire action:
# IMAGE:e_Admiration.jpg
# HEAD:-5,0,0,200
# ARMS:-89,89,2000
# Green feedback
# ============================================================

def admire():
    print("\n--- ADMIRE ---")

    # Admiration expression
    show_face(ADMIRE_FACE)

    # Admire head tilt at velocity 100
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

    # Pure green
    set_colour(GREEN)

    # Hold the Admire behaviour
    time.sleep(2)


# ============================================================
# LOOK AT PAPER BIN
#
# Paper bin is LEFT and BELOW Binnie
# ============================================================

def look_at_paper_bin():
    print("\n--- LOOKING AT PAPER BIN ---")

    move_head(
        pitch=18,      # Down
        roll=0,
        yaw=30,        # Farther LEFT
        velocity=95
    )

    # Keep gaze on paper bin
    time.sleep(1.5)


# ============================================================
# HEAD BACK TO NORMAL
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
# CELEBRATION
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

    # Both arms fully up
    move_arms(
        left=-29,
        right=-29,
        velocity=80
    )

    time.sleep(0.5)

    # Multicoloured lights
    for _ in range(3):
        for colour in celebration_colours:
            set_colour(colour)
            time.sleep(0.2)

    # Hold arms up
    time.sleep(1.5)


# ============================================================
# SCENARIO 1
# ============================================================

if __name__ == "__main__":

    print("\n==============================")
    print("BINNIE - SCENARIO 1")
    print("==============================")

    # ========================================================
    # START
    # Default expression + body reset + blue
    # ========================================================

    reset_body()

    time.sleep(START_PAUSE)

    # ========================================================
    # BEGIN INTERACTION
    # ========================================================

    speak("Let's look at it together.")

    time.sleep(SHORT_PAUSE)


    # ========================================================
    # ASK ABOUT MATERIAL
    # ========================================================

    speak("What do you think it's made of?")

    # CHILD ANSWERS
    time.sleep(CHILD_RESPONSE_PAUSE)


    # ========================================================
    # ASK WHICH BIN
    # ========================================================

    speak(
        "That's right! "
        "Which bin do you think it belongs in?"
    )

    # CHILD SAYS / POINTS TO PAPER BIN
    time.sleep(CHILD_RESPONSE_PAUSE)


    # ========================================================
    # CHILD GETS IT RIGHT
    # Admire + pure green
    # ========================================================

    admire()

    speak("Yes! You figured it out!")

    time.sleep(SHORT_PAUSE)


    # ========================================================
    # LOOK TOWARDS PAPER BIN
    # LEFT 75 + DOWN
    # Velocity = 100
    # ========================================================

    look_at_paper_bin()


    # ========================================================
    # CHILD PHYSICALLY DISPOSES OF ITEM
    # ========================================================

    time.sleep(DISPOSAL_PAUSE)


    # ========================================================
    # HEAD RETURNS TO CENTRE
    # Velocity = 100
    # ========================================================

    centre_head()

    time.sleep(0.5)


    # ========================================================
    # FINAL DIALOGUE
    # ========================================================

    speak("Great job! You Rock!")

    time.sleep(0.8)


    # ========================================================
    # FINAL CELEBRATION
    # Disco lights + both arms fully up
    # ========================================================

    celebrate()

    time.sleep(END_PAUSE)


    # ========================================================
    # RETURN TO DEFAULT
    # ========================================================

    reset_body()

    print("\nScenario 1 complete.")