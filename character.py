# Anil Gurbuz - 29628792
# 16.05.2018 - 27.03.2018
# In this task first pandas and numpy libraries are
# imported to create data structures
# CharacterAnalyser class gets a tokenised list and
# stores number of occurences of each character in
# its own Data Frame



import pandas as pd
import numpy as np

class CharacterAnalyser:
    def __init__(self):
        self.char_df= pd.DataFrame(np.array([0]*52).reshape((52,1)),
                                   index=['A', 'B','C','D','E',
                                          'F', 'G','H','I','J',
                                          'K', 'L','M','N','O',
                                          'P', 'Q','R','S','T',
                                          'U', 'V','W','X','Y',
                                          'Z', '0','1','2','3',
                                          '4', '5','6','7','8',
                                          '9', ',','.','?',';',
                                          ':', "'",'!','-','"',
                                          '(', ')','...'  ,'[',
                                          ']', '+', '&'],
                                   columns=['Number of occurence'])

    def __str__(self):
        string=''
        for i in self.char_df.index:
            string = string + i + ':' + str(self.char_df['Number of occurence'][i]) + '\n' # takes every index and its corresponding value
                                                                                           # then stores it as a string
        return string


    def analyse_characters(self, tokenised_list):


        for i in tokenised_list:     # Takes every token
            upper_tokens= i.upper()  # Makes every token uppercase

            for j in upper_tokens:   # Takes every character of a token
                self.char_df['Number of occurence'][j] += 1    # adds 1 to value of character at dataframe of CharacterAnalyser


    def get_punctuation_frequency(self):
        return self.char_df[36:52]    # Chooses the rows that stores occurences of punctuations