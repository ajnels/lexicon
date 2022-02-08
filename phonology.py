
class Phonology:

    def __init__(self):
        self.language = ''
        self.constants = ''
        self.vowels = ''
        self.onset = ''
        self.nucleus = ''
        self.coda = ''

    def read_phonology(self):
        if self.language is None:
            raise Exception("Need a language defined")

        sounds = []
        file_name = f"languages/{self.language}/phonology.txt"
        file = open(file_name, 'r')
        lines = file.readlines()
        for line in lines:
            sounds.append([c.strip() for c in line.split(',')])

        self.constants = sounds[0]
        self.vowels = sounds[1]
        self.onset = sounds[2]
        self.nucleus = sounds[3]
        self.coda = sounds[4]

    def change_language(self, language):
        self.language = language
        self.read_phonology()
