#!/usr/bin/python3

import json

def load_responses_from_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["responses"]

def save_responses_to_file(file_path, responses):
    data = {"responses": responses}
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def add_response(responses, response, keywords, single_response=False, required_words=None):
    new_response = {
        "response": response,
        "keywords": keywords,
        "single_response": single_response,
    }
    if required_words:
        new_response["required_words"] = required_words
    responses.append(new_response)

def modify_response(responses, index, response=None, keywords=None, single_response=None, required_words=None):
    if response is not None:
        responses[index]["response"] = response
    if keywords is not None:
        responses[index]["keywords"] = keywords
    if single_response is not None:
        responses[index]["single_response"] = single_response
    if required_words is not None:
        responses[index]["required_words"] = required_words

def delete_response(responses, index):
    del responses[index]

def print_responses(responses):
    for idx, response in enumerate(responses):
        print(f"{idx+1}. {response['response']}")
        print(f"   Keywords: {response['keywords']}")
        if 'single_response' in response:
            print(f"   Single Response: {response['single_response']}")
        if 'required_words' in response:
            print(f"   Required Words: {response['required_words']}")
        print()

def main():
    file_path = "responses.json"

    responses = load_responses_from_file(file_path)

    while True:
        print("\n---- Current Responses ----")
        print_responses(responses)

        print("1. Add Response")
        print("2. Modify Response")
        print("3. Delete Response")
        print("4. Save and Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            response = input("Enter the response: ")
            keywords = input("Enter keywords (comma-separated): ").split(",")
            single_response = input("Is it a single response? (True/False): ").lower() == "true"
            required_words = input("Enter required words (comma-separated, optional): ").split(",")
            add_response(responses, response, keywords, single_response, required_words)
        elif choice == "2":
            index = int(input("Enter the index of the response to modify: ")) - 1
            if 0 <= index < len(responses):
                response = input("Enter the modified response: ")
                keywords = input("Enter modified keywords (comma-separated): ").split(",")
                single_response = input("Is it a single response? (True/False): ").lower() == "true"
                required_words = input("Enter modified required words (comma-separated, optional): ").split(",")
                modify_response(responses, index, response, keywords, single_response, required_words)
            else:
                print("Invalid index.")
        elif choice == "3":
            index = int(input("Enter the index of the response to delete: ")) - 1
            if 0 <= index < len(responses):
                delete_response(responses, index)
            else:
                print("Invalid index.")
        elif choice == "4":
            save_responses_to_file(file_path, responses)
            print("Responses saved. Exiting.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

