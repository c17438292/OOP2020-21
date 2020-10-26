# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)
        self.user_input = self.user_input.split()
        print("The user input was: ", self.user_input)
        copy = ""
        i = 0

        for i in range(len(self.user_input)):

            if len(self.user_input[i]) > 3:

                word = list(self.user_input[i])
                k = 0
                temp = word[k]
                word[k]=word[k+1]
                word[k+1]=temp

                j = len(word)

                temp2 = word[j-1]
                word[j-1] = word[j-2]
                word[j-2] = temp2
                self.user_input[i] = word

        print(self.user_input)









        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

