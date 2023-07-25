#!/usr/bin/python3

"""
"""

import random


def unknown():
    """
    """
    response = ["Could you please re-phrase that? ",
                "...",
                "I did not understand that, pardon?",
                "What does that mean?"][
                random.randrange(4)]
    return response

def exit_words():
    """
    """
    response = ["Goodbye! It was nice chatting with you.",
                "Thanks for the conversation! Take care!",
                "I'm just but a humble chatbot. Beep boop beep!",
                "Farewell, and may the pursuit of wisdom guide your path."][
                random.randrange(4)]
    return response
