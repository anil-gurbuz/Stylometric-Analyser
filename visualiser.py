# Anil Gurbuz - 29628792
# 16.05.2018 - 27.03.2018
# This task is done to visualise the analysis using matplotlib
# Therefore, first imports it then draws graphs for relative
# frequencies of punctuation , word length, characters and stop words
# for each of 6 texts


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from word import WordAnalyser


input_handle= open('stopwords','r+')  # Stop words are stored again to be used in stop word visualisation

line_list=input_handle.readlines()

i=210
stopword_list=[]

while i <= 1066:
    upper=line_list[i].upper()
    stopword_list.append(upper)
    i +=2


corrected_stopword_list=[]


for i in stopword_list:
    new_string = ''

    for j in range(len(i)-1):
        new_string += i[j]

    corrected_stopword_list.append(new_string)

stopword_list=corrected_stopword_list

real_list=[]

for i in stopword_list:
    if len(i) > 1 :
        real_list.append(i)

stopword_list=real_list

class Analysisvisualiser:

    def __init__(self,all_text_stats):
        self.freq_df=all_text_stats



    def visualise_character_frequency(self):
        list_of_index = []
        for i in range(65, 91):
            list_of_index.append(chr(i))        # chr(65)= 'A' ... chr(90) = 'Z' so this loop creates a list to specify
                                                # the index values of characters in the Dataframe that stores all datas of
                                                # 6 texts
        plt.plot(self.freq_df.loc[list_of_index, ['File1']], label='File1')
        plt.plot(self.freq_df.loc[list_of_index, ['File2']], label='File2')
        plt.plot(self.freq_df.loc[list_of_index, ['File3']], label='File3')
        plt.plot(self.freq_df.loc[list_of_index, ['File4']], label='File4')
        plt.plot(self.freq_df.loc[list_of_index, ['File5']], label='File5')
        plt.plot(self.freq_df.loc[list_of_index, ['File6']], label='File6')
        plt.title('Character Analysis')
        plt.legend()
        plt.savefig('Character Analysis')# To save the output figure
        plt.show()

        #.loc is used to specify rows and columns using list of index and column name values



    def visualise_punctuation_frequency(self):
        list_of_index = [',','.','?',';',':', "'",'!','-','"',
                         '(', ')','...'  ,'[',']', '+', '&']

        plt.plot(self.freq_df.loc[list_of_index, ['File1']], label='File1')
        plt.plot(self.freq_df.loc[list_of_index, ['File2']], label='File2')
        plt.plot(self.freq_df.loc[list_of_index, ['File3']], label='File3')
        plt.plot(self.freq_df.loc[list_of_index, ['File4']], label='File4')
        plt.plot(self.freq_df.loc[list_of_index, ['File5']], label='File5')
        plt.plot(self.freq_df.loc[list_of_index, ['File6']], label='File6')
        plt.title('Punctuation Analysis')
        plt.legend()
        plt.savefig('Punctuation Analysis')# To save the output figure
        plt.show()
        # .loc is used to specify rows and columns using list of index and column name values


    def visualise_stopword_frequency(self):
        list_of_index = stopword_list  # Takes the stop word list( Created at the beginning of the module) to specify the index names of stopwords
                                       # in the Dataframe that stores all datas of 6 texts

        plt.plot(self.freq_df.loc[list_of_index, ['File1']], label='File1')
        plt.plot(self.freq_df.loc[list_of_index, ['File2']], label='File2')
        plt.plot(self.freq_df.loc[list_of_index, ['File3']], label='File3')
        plt.plot(self.freq_df.loc[list_of_index, ['File4']], label='File4')
        plt.plot(self.freq_df.loc[list_of_index, ['File5']], label='File5')
        plt.plot(self.freq_df.loc[list_of_index, ['File6']], label='File6')
        plt.xticks(rotation=90) # makes the labels of x axis perpendicular to x axis in order to make it readable
        plt.title('Stop Word Analysis')
        plt.legend()
        plt.savefig('Stop Word Analysis')# To save the output figure
        plt.show()


    def visualise_word_length_frequency(self):
        list_of_index=[]

        for i in self.freq_df.index:          # Takes all the indexes of the Dataframe that stores all the datas of 6 texts
            if i.find('character/s') != -1:   # Checks is there any index name that includes 'character/s'( This index names
                list_of_index.append(i)       # are created while doing word length analysis. If the searched string is not found
                                              # .find() command returns -1 so if it doesn't returns -1
                                              # index name is added to a list to specify the index names of word lengths
                                              # in the Dataframe that stores all datas of 6 texts.
        plt.plot(self.freq_df.loc[list_of_index, ['File1']], label='File1')
        plt.plot(self.freq_df.loc[list_of_index, ['File2']], label='File2')
        plt.plot(self.freq_df.loc[list_of_index, ['File3']], label='File3')
        plt.plot(self.freq_df.loc[list_of_index, ['File4']], label='File4')
        plt.plot(self.freq_df.loc[list_of_index, ['File5']], label='File5')
        plt.plot(self.freq_df.loc[list_of_index, ['File6']], label='File6')
        plt.xticks(rotation=90)   # makes the labels of x axis perpendicular to x axis in order to make it readable
        plt.title('Word Length Analysis')
        plt.legend()
        plt.savefig('Word Length Analysis') # To save the output figure
        plt.show()