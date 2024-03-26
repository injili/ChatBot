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
    messages = [{"role": "user", "content": prompt}]
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
