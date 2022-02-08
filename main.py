import csv
import os
import re
from random import Random
from phonology import Phonology

language = ''
phonology = Phonology()


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
    if language == '':
        print('Please define a language first')
        change_language()

    if word is None:
        word = input('Word: ')

    part_of_speech = input('Part of Speech: ')
    definition = input('Definition: ')

    if not os.path.exists('languages') or not os.path.isdir('languages'):
        os.mkdir('languages')

    if not os.path.exists(language) or not os.path.isdir(language):
        os.mkdir(language)

    with open(f"languages/{language}/{language}_lexicon.csv", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([word, part_of_speech, definition])
    csv_file.close()


def generate_word():
    word = ""
    random = Random()
    number_syllables = random.randint(1, 4)
    for i in range(number_syllables):
        selected_onset = phonology.onset[random.randint(0, len(phonology.onset) - 1)]
        selected_nucleus = phonology.nucleus[random.randint(0, len(phonology.nucleus) - 1)]

        word += selected_onset + selected_nucleus

    if random.randint(0, 100) < 50:
        selected_coda = phonology.coda[random.randint(0, len(phonology.coda) - 1)]
        word += selected_coda

    forbidden_clusters = ['(c)rh']
    for cluster in forbidden_clusters:
        if '(c)' in cluster:
            cluster = cluster.replace('(c)', '')
            regex = f"{cluster}|".join(phonology.constants) + f"{cluster}"
            word = re.sub(regex, cluster, word)

    print(f"\nWord Generated was: {word}\n")
    user_input = input('Add Word? (Y/N)\n')
    if user_input.lower() == 'g' or user_input.lower() == 'y':
        add_word(word)

    welcome_prompt()


def change_language():
    global language
    language = input("Enter Language to work on:\n")
    phonology.change_language(language)


if __name__ == '__main__':
    welcome_prompt()
