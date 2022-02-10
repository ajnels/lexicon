from random import Random

from WordGenerator import WordGenerator


class EhsithfaWordGenerator(WordGenerator):

    def generate_word(self):
        word = ""
        random = Random()
        number_syllables = random.randint(1, 4)
        for i in range(number_syllables):
            if random.randint(0, 100) < 50:
                selected_onset = self.phonology.onset[random.randint(0, len(self.phonology.onset) - 1)]
                word += selected_onset

            selected_nucleus = self.phonology.nucleus[random.randint(0, len(self.phonology.nucleus) - 1)]
            word += selected_nucleus

            if random.randint(0, 100) < 50:
                selected_coda = self.phonology.coda[random.randint(0, len(self.phonology.coda) - 1)]
                word += selected_coda
        return word
