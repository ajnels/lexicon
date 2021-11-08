import csv
import os

language = ''


def welcome_prompt():
    print('Welcome to Lexicon!')
    print('Change Language')
    print('Add Word')
    print('Quit')
    user_input = input('Enter choice\n')

    if user_input.lower() == 'a':
        add_word()
    elif user_input.lower() == 'l':
        change_language()
    elif user_input.lower() == 'q':
        exit()

    welcome_prompt()


def add_word():
    if language == '':
        print('Please define a language first')
        change_language()

    word = input('Word: ')
    part_of_speech = input('Part of Speech: ')
    definition = input('Definition: ')

    if not os.path.exists('languages') or not os.path.isdir('languages'):
        os.mkdir('languages')

    with open('languages/' + language + '.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([word, part_of_speech, definition])
    csv_file.close()


def change_language():
    global language
    language = input("Enter Language to work on:\n")


if __name__ == '__main__':
    welcome_prompt()
