import os

from Phonology import Phonology


class WordGenerator:

    def __init__(self, language=None):
        self.language = language
        self.phonology = None

        if self.language:
            self.set_language()

    def generate_word(self):
        pass

    def set_language(self):
        self.phonology = Phonology(self.language)

        word_generator_file = f"language_models/{self.language}WordGenerator.py"
        if not os.path.exists(word_generator_file) or not os.path.isfile(word_generator_file):
            raise Exception(f"{self.language}WordGenerator.py does not exist. Please implement before using")
