from random import Random
import re

from WordGenerator import WordGenerator


class KorukWordGenerator(WordGenerator):

    def generate_word(self):
        word = ""
        random = Random()
        number_syllables = random.randint(1, 4)
        for i in range(number_syllables):
            selected_onset = self.phonology.onset[random.randint(0, len(self.phonology.onset) - 1)]
            selected_nucleus = self.phonology.nucleus[random.randint(0, len(self.phonology.nucleus) - 1)]

            word += selected_onset + selected_nucleus

        if random.randint(0, 100) < 50:
            selected_coda = self.phonology.coda[random.randint(0, len(self.phonology.coda) - 1)]
            word += selected_coda

        forbidden_clusters = ['(c)rh']
        for cluster in forbidden_clusters:
            if '(c)' in cluster:
                cluster = cluster.replace('(c)', '')
                regex = f"{cluster}|".join(self.phonology.constants) + f"{cluster}"
                word = re.sub(regex, cluster, word)
        return word
