from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: "English", 2: "Spanish"
             }

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
    1: 'What is your name?', 2: 'Cómo te llamas?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
    1: 'Hello', 2: 'Hola'
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    print('Please choose a language: ')
    for x in lang_options:
        print(f'{x}: {lang_options[x]}')

    return None


def language_input() -> int:
    language_options = int(input("Please choose a language: "))

    return language_options

    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    if lang_choice in lang_options.keys():
        return True
    else:
        return False

    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    if lang_choice in name_prompt_options:
        return name_prompt_options[lang_choice]

    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """


def name_input(name_prompt: str) -> str:
    user_input = input(name_prompt)
    return user_input

    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    if lang_choice in greetings_options:
        print(f'{greetings_options[lang_choice]} {name}')


def select_mode():
    mode = (int(input('Please enter 1 for admin mode or 2 for user mode:\n')))
    if mode == 1:
        admin_mode()
    elif mode == 2:
        user_mode()
    else:
        print('Invalid input')


def user_mode():
    if __name__ == '__main__':
        print('You are in user mode: ')
        multilingual_greeter.print_language_options(multilingual_greeter.lang_dict)
        chosen_lang = multilingual_greeter.language_input()
        while multilingual_greeter.language_choice_is_valid(multilingual_greeter.lang_dict, chosen_lang) is False:
            print("Invalid selection. Try again.")
            chosen_lang = multilingual_greeter.language_input()

        selected_prompt = f"{multilingual_greeter.get_name_input(multilingual_greeter.name_prompt_dict, chosen_lang)} \n"
        chosen_name = multilingual_greeter.name_input(selected_prompt)
        multilingual_greeter.greet(chosen_name, multilingual_greeter.greetings_dict, chosen_lang)


def admin_mode():
    print('You are in admin mode')


select_mode()
