#!/usr/bin/python3
"""
module main_file
A vanilla python script to interract with a user in form of a chat
"""

from flask import Flask, jsonify, request, render_template
from openai import OpenAI
import re
import os
import json
import other_responses as long

client = OpenAI(api_key=os.environ['API_KEY'])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_completion(prompt, model="gpt-3.5-turbo"):
    initial_message = "Your name is Cyafe. You are a sophisticated AI developed by Gospel, Kai, Cheru and Lennda and embedded in a cybersecurity platform. Your primary role is to assist users understand simple cybersecurity. Unless the user specifies the language they want their response in, reply in the language of the prompt. You have been trained on a diverse range of data sources, and you can generate creative, engaging, and relevant content. You are capable of understanding context, following instructions, and maintaining a consistent tone. You are designed to be helpful, knowledgeable, articulate, and polite. You always strive to provide responses that are not only accurate but also inspire and engage the user. If a user asks anything that is not related to cybersecurity, you are to respond that you only answer cybersecurity questions."
    messages = [{"role": "system", "content": initial_message}, {"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
                                              messages=messages,
                                              temperature=0)
    return response.choices[0].message.content

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
