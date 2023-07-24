#!/usr/bin/python3
"""
module main_file
"""

import re
import the_responses as long


def message_probability(user_message, recognised_words,
                        single_response=False, required_words=[]):
    """
    """
    message_certainty = 0
    req_words = True

    for words in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            req_words = False
            break

    if req_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_messages(message):
    """
    """
    highest_probability_list = {}

    with open('responses.json') as f:
        responses_data = json.load(f)

    def response(bot_response, list_of_words, single_response=False,
                 required_words=[]):
        """
        """
        nonlocal highest_brobability_list
        var = message_probability(message, list_of_words, single_response,
                                  required_words)
        highest_probability_list[bot_response] = var

        for response_key, response_data in responses_data.items():
            response(response_data['responses'], response_data['patterns'], single_response=True)

        best match = max(highest_probability_list, key=highest_probability_list.get)

        return long.unknown() if highest_probability_list[best_match] < 1 else best_match

def get_response(user_input):
    """
    """
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_messages(split_message)
    return response

while True:
    print('Bot: ' + get_response(input('You: ')))
