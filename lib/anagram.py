# your code goes here!
class Anagram:
    def __init__(self, word):
        # store the word in lowercase for consistent comparison
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        # sort the base word's letters once to avoid sorting it repeatedly
        sorted_base = sorted(self.word)

        for candidate in word_list:
            # ignore identical words
            if candidate.lower() != self.word:
                if sorted(candidate.lower()) == sorted_base:
                    matches.append(candidate)

        return matches
