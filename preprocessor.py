# Anil Gurbuz - 29628792
# 16.05.2018 - 27.03.2018
# In this task, Preprocessor class's tokenise module
# takes a sequence turns it into a list
# that is created by splitting the sequence due to spaces in the sequence
# And get_tokenised_list module returns the tokenised list

class Preprocessor:

    def __init__(self):
        self.tokens_list=[]

    def __str__(self):
        return str(len(self.tokens_list))

    def  tokenise(self, input_sequence):
        self.tokens_list = input_sequence.split(' ')


    def get_tokenised_list(self):
        return self.tokens_list
