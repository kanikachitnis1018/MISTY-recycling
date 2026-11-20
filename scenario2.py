import requests
import time

ROBOT_IP = "192.168.0.248"
BASE_URL = f"http://{ROBOT_IP}/api"

# ============================================================
# TIMING
# ============================================================

START_PAUSE = 2
CHILD_RESPONSE_PAUSE = 4
THINKING_PAUSE = 3
DISPOSAL_PAUSE = 3
SHORT_PAUSE = 4
END_PAUSE = 3

# ============================================================
# COLOURS / EXPRESSIONS
# ============================================================

BLUE = (0, 100, 255)
YELLOW = (255, 180, 0)
GREEN = (0, 255, 0)

DEFAULT_FACE = "e_DefaultContent.jpg"
CONFUSED_FACE = "e_Terror.jpg"
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
# Arms down + head centre + default face + blue light
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

    # Default expression
    show_face(DEFAULT_FACE)

    # Blue listening light
    set_colour(BLUE)

    # Give physical movements time to finish
    time.sleep(2)


# ============================================================
# CONFUSED
#
# Based on Binnie's Confused action:
# IMAGE:e_Terror.jpg
# HEAD:-5,25,0
# HEAD:-5,-25,0
# HEAD:-5,0,0
#
# Arms deliberately do NOT move here.
# ============================================================

def confused():
    print("\n--- CONFUSED ---")

    # Yellow = wrong / "not yet"
    set_colour(YELLOW)

    # Confused face
    show_face(CONFUSED_FACE)

    # Head tilt one direction
    move_head(
        pitch=-5,
        roll=25,
        yaw=0,
        velocity=100
    )

    time.sleep(1.5)

    # Head tilt other direction
    move_head(
        pitch=-5,
        roll=-25,
        yaw=0,
        velocity=100
    )

    time.sleep(1.5)

    # Head back to centre
    move_head(
        pitch=-5,
        roll=0,
        yaw=0,
        velocity=100
    )

    time.sleep(1)


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
# LOOK AT LANDFILL BIN
#
# Currently assumes landfill is in front of Binnie.
# ============================================================

def look_at_landfill_bin():
    print("\n--- LOOKING AT LANDFILL BIN ---")

    move_head(
        pitch=18,
        roll=0,
        yaw=0,
        velocity=100
    )

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
# Both arms UP + disco lights
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
# SCENARIO 2 - USED PAPER TOWEL
# ============================================================

if __name__ == "__main__":

    print("\n==============================")
    print("BINNIE - SCENARIO 2")
    print("USED PAPER TOWEL")
    print("==============================")


    # ========================================================
    # START WITH COMPLETE RESET
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

    # CHILD: "Paper"
    time.sleep(CHILD_RESPONSE_PAUSE)


    # ========================================================
    # ASK WHICH BIN
    # ========================================================

    speak(
        "That's right! It's paper. "
        "Which bin do you think it belongs in?"
    )

    # CHILD INCORRECTLY SAYS PAPER RECYCLING
    time.sleep(CHILD_RESPONSE_PAUSE)


    # ========================================================
    # WRONG ANSWER
    # Yellow + Confused
    # ========================================================

    confused()

    speak("Almost! Take another look at the paper towel.")

    time.sleep(SHORT_PAUSE)

    speak("Has it already been used?")

    # CHILD: "Yes"
    time.sleep(CHILD_RESPONSE_PAUSE)


    # ========================================================
    # RETURN TO LISTENING
    # ========================================================

    show_face(DEFAULT_FACE)
    set_colour(BLUE)
    centre_head()


    # ========================================================
    # GIVE HINT
    # ========================================================

    speak(
        "That's right. Think about whether "
        "this can still be recycled."
    )

    # CHILD THINKS
    time.sleep(THINKING_PAUSE)


    # ========================================================
    # ASK FOR BIN AGAIN
    # ========================================================

    speak("So, which bin do you think it goes in?")

    # CHILD: "Landfill"
    time.sleep(CHILD_RESPONSE_PAUSE)


    # ========================================================
    # CHILD GETS IT RIGHT
    # Admire + pure green
    # ========================================================

    admire()

    speak("Yes! You figured it out!")

    time.sleep(SHORT_PAUSE)


    # ========================================================
    # LOOK TOWARDS LANDFILL BIN
    # ========================================================

    look_at_landfill_bin()


    # ========================================================
    # CHILD PHYSICALLY DISPOSES OF PAPER TOWEL
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
    # Both arms up + disco lights
    # ========================================================

    celebrate()

    time.sleep(END_PAUSE)


    # ========================================================
    # FULL RESET
    # ========================================================

    reset_body()

    print("\nScenario 2 complete.")