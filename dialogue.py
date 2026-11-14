# dialogue.py
import random

class DialogueEngine:
    @staticmethod
    def get_greeting() -> str:
        return "Hi there! Hold up an item in front of my camera, and let's figure out where it goes!"

    @staticmethod
    def get_prompt(item_name: str = "this item") -> str:
        prompts = [
            f"Ooh, I see {item_name}! Which bin do you think it goes in?",
            f"Interesting! You are holding {item_name}. Which bin should we put it in?",
            f"Let's sort {item_name}! Point or move it toward the right bin."
        ]
        return random.choice(prompts)

    @staticmethod
    def get_hint(expected_category: str) -> str:
        hints = {
            "paper": "Not quite! Look closely—is it made of paper or cardboard? Try the paper bin!",
            "recycling": "Hmm, not that one! Clean plastic bottles and metal cans can be recycled. Try again!",
            "landfill": "Oops, not quite! Dirty wrappers or mixed trash cannot be recycled. Which bin is for regular trash?"
        }
        return hints.get(expected_category, "Let's think carefully and try another bin!")

    @staticmethod
    def get_praise(expected_category: str) -> str:
        praises = [
            f"Yes! Great job! That goes right into {expected_category}!",
            f"Woohoo! You nailed it! {expected_category.capitalize()} is the right bin!",
            f"Awesome job! You are a sorting superstar!"
        ]
        return random.choice(praises)