# Misty Recycling HRI Project

This project uses the Misty II social robot to explore an interactive approach to teaching waste sorting. Misty guides users through sorting items into three categories:

- Paper
- Recycling (glass, metal, and plastic)
- Landfill

The repository contains two implementations of the same interaction design.

## vision\-pipeline

The vision\-pipeline branch explores automatic item recognition using Misty's camera.

### Flow

**Present item → Capture image → Compare with reference images → Identify item/category → Misty responds**

### Main Components

- main.py — application entry point
- misty\_client.py — communication with Misty
- classifier.py — image recognition
- categories.py — category definitions
- dialogue.py — dialogue and feedback
- reference\_images/ — known object images
- config.py — local configuration

---

## wizard\-of\-oz

The wizard\-of\-oz branch removes the requirement for automatic item recognition. Instead, an operator observes the participant and triggers a predefined Paper, Recycling, or Landfill scenario.

Misty then behaves as though the item has been identified.

### Flow

**Present item → Wizard selects scenario → Misty asks participant → Participant chooses bin → Wizard marks correct/incorrect → Misty provides feedback**

Correct decisions receive positive feedback and reinforcement. Incorrect decisions receive a supportive hint followed by another opportunity to choose.

### Main Components

- main.py — application entry point
- woz\_controller.py — operator controls and scenario execution
- scenarios.json — predefined interactions
- misty\_client.py — communication with Misty
- dialogue.py — dialogue and educational prompts
- config.py — local configuration

---

## HRI Design

Both implementations use the same interaction principles:

- Joint attention between Misty, the user, and the object
- Multimodal feedback using speech, LEDs, expressions, and movement
- Positive reinforcement for correct decisions
- Supportive hints rather than immediate correction
- Opportunities for users to reconsider incorrect choices
- Encouraging independent waste\-sorting decisions

## Switching Branches

Vision pipeline:

git switch vision\-pipeline

Wizard of Oz:

git switch wizard\-of\-oz

Check the active branch:

git branch

