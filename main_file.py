#!/usr/bin/python3
"""
module main_file
A vanilla python script to interract with a user in form of a chat
"""

from flask import Flask, jsonify, request, render_template
import re
import json
import other_responses as long

app = Flask(__name__)


def message_probability(user_message, recognised_words,
                        single_response=False, required_words=[]):
    """
    calculate the message probability and return the percentage
    Args:
        user_message(str): The message typed by the user
        recognised_words(list of str): The keywords to be sought in the message
        single_response(bool): If True, bypasses the required_words check
        required_words(str list): Words that have to be in the message
    """
    message_certainty = 0
    req_words = True

    for word in user_message:
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
    Does the check on the message tofind the most suitable response
    Args:
        message(str): The message by the user
    """
    highest_probability_list = {}

    with open('responses.json') as f:
        responses_data = json.load(f)
        responses_list = responses_data.get('responses', [])

    def response(bot_response, list_of_words, single_response=False,
                 required_words=[]):
        """
        A function to calculate and store the message probability for a response
        Args:
            bot_response(str): A response from the json file.
            list_of_words(list of str): A list of keywords to match the response
            single_response(bool): Determines whether only one word is needed for the match
            required_words(list of str): Words that must be present in the message if the
                response isn't a single_response category
        """
        nonlocal highest_probability_list
        var = message_probability(message, list_of_words, single_response,
                                  required_words)
        highest_probability_list[bot_response] = var

    for response_data in responses_list:
        response(response_data['response'], response_data['keywords'],
                 response_data.get('single_response', False),
                 response_data.get('required_words', []))

    best_match = max(highest_probability_list,
                     key=highest_probability_list.get)
    return (
            long.unknown()
            if highest_probability_list[best_match] < 1
            else best_match
            )


def get_response(user_input):
    """
    Fetches the response and passes it back
    Args:
        user_input(str): The query typed in by the user
    """
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_messages(split_message)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_chatbot_response', methods=['POST'])
def get_chatbot_response():
    user_input = request.form['user_input']
    return jsonify({'bot_response': get_response(user_input)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
