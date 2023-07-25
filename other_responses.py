#!/usr/bin/python3

"""
module other_responses
A script to store specific random responses for specific scenarios
"""

import random


def unknown():
    """
    Responses for when the text typed in hasn't been understood
    """
    response = ["Could you please re-phrase that?",
                "...",
                "I did not understand that, pardon?",
                "What does that mean?"][
                random.randrange(4)]
    return response

def exit_words():
    """
    Responses for when the program exits
    """
    response = ["Goodbye! It was nice chatting with you.",
                "Thanks for the conversation! Take care!",
                "I'm just but a humble chatbot. Beep boop beep!",
                "Farewell, and may the pursuit of wisdom guide your path."][
                random.randrange(4)]
    return response
