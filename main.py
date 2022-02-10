import csv
import os
import importlib
from WordGenerator import WordGenerator

word_generator = WordGenerator()


def welcome_prompt():
    print('Welcome to Lexicon!')
    print('Change (L)anguage')
    print('(A)dd Word')
    print('(G)enerate Word')
    print('(Q)uit')
    user_input = input('Enter choice\n')

    if user_input.lower() == 'a':
        add_word()
    elif user_input.lower() == 'l':
        change_language()
    elif user_input.lower() == 'g':
        generate_word()
    elif user_input.lower() == 'q':
        exit()

    welcome_prompt()


def add_word(word=None):
    check_language()

    if word is None:
        word = input('Word: ')

    part_of_speech = input('Part of Speech: ')
    definition = input('Definition: ')

    language_path = f"language_data/{word_generator.language}"
    if not os.path.exists(language_path) or not os.path.isdir(language_path):
        os.mkdir(language_path)

    with open(f"{language_path}/{word_generator.language}_lexicon.csv", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([word, part_of_speech, definition])
    csv_file.close()


def generate_word():
    check_language()

    word = word_generator.generate_word()
    print(f"\nWord Generated was: {word}\n")

    user_input = input('Add Word? (Y/N)\n')
    if user_input.lower() == 'g' or user_input.lower() == 'y':
        add_word(word)

    welcome_prompt()


def change_language():
    language = input("Enter Language to work on:\n")
    try:
        global word_generator
        module = importlib.import_module(f"language_models.{language}WordGenerator")
        class_ = getattr(module, f"{language}WordGenerator")
        word_generator = class_(language)
    except Exception as e:
        print(f"Uh-oh something went wrong: {e}")
        print(f"Try selecting a predefined language")
        change_language()


def check_language():
    if not word_generator or not word_generator.language:
        print('Please define a language')
        change_language()


if __name__ == '__main__':
    welcome_prompt()
