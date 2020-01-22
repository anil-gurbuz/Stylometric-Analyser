# Anil Gurbuz - 29628792
# 16.05.2018 - 27.03.2018
# In this task first pandas and numpy libraries are
# imported to create data structures and urllib.request
# is imported to retrieve the content of a web page which stores
# stop words. This module makes analysis to find number of
# occurrences of each word , each stop word and each word length
# in the tokenised list.




import pandas as pd
import numpy as np
import urllib.request


url="http://www.lextek.com/manuals/onix/stopwords1.html"
local_filename="stopwords"


urllib.request.urlretrieve(url,local_filename) # Takes the content of url and stores it in the pre-defined file

input_handle= open('stopwords','r+') # Opens the file and stores it on input_handle variable

line_list=input_handle.readlines() # Takes every line of input_handle and stores it as a list

i=210 # Stop words starts at 210. line so variable starts from 210
stopword_list=[] # list that will store all the stop words

while i <= 1066:  # Last stop word is at 1066. line
    upper=line_list[i].upper()
    stopword_list.append(upper)
    i +=2 # In the URL there are 1 empty line between two stopwords so i is increased by 2 for every step of loop


corrected_stopword_list=[] # every stopword comes from web page with \n at the end , this list created to correct it


for i in stopword_list:
    new_string = ''

    for j in range(len(i)-1):# Takes every character of every word except for last character which is \n
        new_string += i[j]   # Stores them on the string

    corrected_stopword_list.append(new_string) # adds to string to list

stopword_list=corrected_stopword_list

real_list=[]  # Created to store the stopwords that are longer than 1 character

for i in stopword_list:  # Gets every Word from stopword list
    if len(i) > 1 :      # Checks is it longer than 1 character, if so adds it to real list
        real_list.append(i)

stopword_list=real_list





class WordAnalyser:
    def __init__(self):
        self.word_df= pd.DataFrame(columns=['Word count']) # Empty Dataframe to store the words in the text



    def __str__(self):
        string=''
        for i in self.word_df.index:
            string = string + i + ':' + str(self.word_df['Word count'][i]) + '\n'# takes every index and its corresponding value
                                                                                 # then stores it as a string
        return string


    def analyse_words(self,tokenised_list):

        upper_tokenised_list=[]

        for each_element in tokenised_list:
            if each_element not in [',','.','?',';', ':', "'",'!','-','"','(',')','...','[', ']', '+', '&']:
                upper_tokenised_list.append(each_element.upper())

        indexes_set = set(upper_tokenised_list) # Turns the words list into set in order to create a list for indexes


        indexes_list=list(indexes_set)

        self.word_df=pd.DataFrame(np.array([0]*len(indexes_list)).reshape((len(indexes_list),1))  # Creates a data frame and sets the indexes as occured words in the text
                                  ,columns=['Word count'],                                        # number of rows are specified with the number of indexes
                                   index= indexes_list)

        for each_word in upper_tokenised_list:          # Takes the tokenised list one by one and adds 1 to corresponding value
            self.word_df['Word count'][each_word] +=1   # of the word in Data frame created above

        self.word_df['Word count']=self.word_df['Word count'].astype(int) # Turns the type of the values from float to number in order to get rid of the numbers after point
                                                                          # because there can not be any number of occurence thats not an integer


    def stop_word_frequency(self):
        stop_word_df=pd.DataFrame() # Empty data frame created to store stopwords as indexes

        for each_index in self.word_df.index:                                   # Takes every word from pre-defined dataframe
            if each_index in stopword_list:                                     # And Checks for  every word whether its a stopword or not
                stop_word_df=stop_word_df.append(self.word_df.loc[each_index])  # If so, stores it on pre-created Dataframe as indexes

        stop_word_df['Word count']=stop_word_df['Word count'].astype(int)       # Turns the type of the values from float to number in order to get rid of the numbers after point
                                                                                # because there can not be any number of occurence thats not an integer

        return stop_word_df


    def get_word_length_frequency(self):
        length_of_words=[]

        for each_index in self.word_df.index:           # Takes every word from pre-defined Dataframe
            if len(each_index) not in length_of_words:  # Checks every words length and creates a list to use
                length_of_words.append(len(each_index)) # as index values in the following steps

        list_of_indexes_of_word_length_df=[]
        length_of_words.sort()                      # Sorts the list to have sorted index values

        for each_length in length_of_words:         # Gets every word length occurred in the text
            new =''
            new =  str(each_length) + 'character/s'         # Creates a more readable string to be used
            list_of_indexes_of_word_length_df.append(new)   # as indexes in the following steps


        word_length_freq_df=pd.DataFrame(index=list_of_indexes_of_word_length_df, # Data frame created with word lengths as indexes
                                            columns=['Number of words'])

        word_length_freq_df=word_length_freq_df.fillna(0)                         # In order to get ride of nan values

        for each_word in self.word_df.index:
            word_length_freq_df['Number of words'][str(len(each_word))+'character/s'] +=1    # For each of words , adds 1 to coressponding word length using the same format
                                                                                             # of indexes of dataframe.


        return word_length_freq_df

