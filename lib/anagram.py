# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=word.lower()
    def match(self, possible_anagrams):
        matches=[]
        sorted_word=sorted(self.word)
        for candidate in possible_anagrams:
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)
        return matches
