#!/usr/bin/python3

"""
module write responses
A script that exists to modify and customise the responses of the bot
"""
import json


def load_responses_from_file(file_path):
    """
    Read responses from the json file passed to be modified

    Args:
        file_path(file): The json file to be read
    """
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["responses"]


def save_responses_to_file(file_path, responses):
    """
    Save onto the json file the changes made

    Args:
        file_path(file): The json file being modified
        responses(dictionary): The responses to be written
    """
    data = {"responses": responses}
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


def add_response(responses, response, keywords,
                 single_response=False, required_words=None):
    """
    Add new entry onto the json structure

    Args:
        responses(list of dict): The list with the responses
        response(str): The response message to be added
        keywords(list of str): The keywords associated to the response
        single_response(optional, boolean): True or false depending on
                    the response
        required_words(optional, str list): The words needed for a
                    response to be selected
    """
    new_response = {
        "response": response,
        "keywords": keywords,
        "single_response": single_response,
    }
    if required_words:
        new_response["required_words"] = required_words
    responses.append(new_response)


def modify_response(responses, index, response=None, keywords=None,
                    single_response=None, required_words=None):
    """
    Modify an already existing response

    Args:
        responses(list of dict): The list of all responses
        index(int): The index of the specific response to be modified
        response(optional, str): The updated response
        keywords(optional, dict): The new keywords
        single_response(optional, bool): True or False
        required_words(optional, dict): Words that'll have to be there

    If any of the optional parameters are not proovided, the file will
    default to the orriginal values at the specified index.
    """
    if response is not None:
        responses[index]["response"] = response
    if keywords is not None:
        responses[index]["keywords"] = keywords
    if single_response is not None:
        responses[index]["single_response"] = single_response
    if required_words is not None:
        responses[index]["required_words"] = required_words


def delete_response(responses, index):
    """
    Delete a dict from the responses

    Args:
        responses(list of dict): all the responses
        index(int): A specified entry to be deleted from the responses
    """
    del responses[index]


def print_responses(responses):
    """
    Print out all the responses for the Admin

    Args:
        responses(dict list): All of the responses
    """
    for idx, response in enumerate(responses):
        print(f"{idx+1}. {response['response']}")
        print(f"   Keywords: {response['keywords']}")
        if 'single_response' in response:
            print(f"   Single Response: {response['single_response']}")
        if 'required_words' in response:
            print(f"   Required Words: {response['required_words']}")
        print()


def main():
    """
    The main function to this script
    """
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
