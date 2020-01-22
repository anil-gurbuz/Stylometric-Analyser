# Anil Gurbuz - 29628792
# 16.05.2018 - 27.03.2018
# This module is the module that contains all other tasks to
# create the whole program
# get_input() function prompts the user to enter the names/paths of text files
# that will be analysed then in the main() function all other classes' instances
# are created and used to make all analyses and to draw all needed graphs.



import pandas as pd
import numpy as np
import urllib.request
from preprocessor import Preprocessor
from character import CharacterAnalyser
from word import WordAnalyser
from visualiser import Analysisvisualiser


def read_input():
    choice=input('Please enter the  location of files with one spaces between names: \n'
          ' If the files are in the same directory with python project it is enough to enter just file names instead of locations \n'
          'For example: Edward_II_Marlowe.tok Jew_of_Malta_Marlowe.tok Richard_II_Shakespeare.tok Hamlet_Shakespeare.tok Henry_VI_Part1_Shakespeare.tok Henry_VI_Part2_Shakespeare.tok  ')

    choice_list= choice.split(' ')
    list_of_files=[]

    for every_text in choice_list:
        input_handle = open(every_text, 'r+')   # Opens every text
        line_list = input_handle.readlines()    # stores every lines of text as a list of strings

        new_list=[]
        for each_line in line_list:             # Purpose of this loop is to get rid of the character(\n) at the end of all lines
            string=''
            for i in range(len(each_line)-1): # Last character of line is not taken because there is \n at the end of each line
                string += each_line[i]

            new_list.append(string.upper())

        file=''
        for each_line in new_list:   # This loop turns list of strings into one string
            file += each_line + ' '  # Beacues preprocessor will take string as an argument

        file=file.strip()            # Because of the space added after every line in previous step
                                     # There is an extra space at the end of the text  and this .strip() removes it

        list_of_files.append(file)   # List_of_files stores whole text as one string and string of all texts are one of the  element of the list.


    return list_of_files


def main():

    list_of_files = read_input() # Takes the input from user and returns a list of strings each stores whole string of one text

    File1 = list_of_files[0] # Takes every string and assign it to a variable
    File2 = list_of_files[1] # with entry order
    File3 = list_of_files[2]
    File4 = list_of_files[3]
    File5 = list_of_files[4]
    File6 = list_of_files[5]

    proces1 = Preprocessor() # Creates 6 instances of Preprocessor class (each one is for different files)
    proces2 = Preprocessor()
    proces3 = Preprocessor()
    proces4 = Preprocessor()
    proces5 = Preprocessor()
    proces6 = Preprocessor()

    character1 = CharacterAnalyser() # Creates 6 instances of CharacterAnalyser class (each one is for different files
    character2 = CharacterAnalyser()
    character3 = CharacterAnalyser()
    character4 = CharacterAnalyser()
    character5 = CharacterAnalyser()
    character6 = CharacterAnalyser()

    word1 = WordAnalyser()   # Creates 6 instances of WordAnalyser class (each one is for different files
    word2 = WordAnalyser()
    word3 = WordAnalyser()
    word4 = WordAnalyser()
    word5 = WordAnalyser()
    word6 = WordAnalyser()

    proces1.tokenise(File1)  # Tokenises every indivudual text file which is turned into a string in get_input function
    proces2.tokenise(File2)
    proces3.tokenise(File3)
    proces4.tokenise(File4)
    proces5.tokenise(File5)
    proces6.tokenise(File6)

    tokenlist1 = proces1.get_tokenised_list() # Assigns to tokenised lists to a variable
    tokenlist2 = proces2.get_tokenised_list()
    tokenlist3 = proces3.get_tokenised_list()
    tokenlist4 = proces4.get_tokenised_list()
    tokenlist5 = proces5.get_tokenised_list()
    tokenlist6 = proces6.get_tokenised_list()

    character1.analyse_characters(tokenlist1) # Analysis characters for every tokenised list
    character2.analyse_characters(tokenlist2)
    character3.analyse_characters(tokenlist3)
    character4.analyse_characters(tokenlist4)
    character5.analyse_characters(tokenlist5)
    character6.analyse_characters(tokenlist6)


    sum1 = character1.char_df.values.sum()  # Finds the total  number of occurence of characters in the text
    sum2 = character2.char_df.values.sum()
    sum3 = character3.char_df.values.sum()
    sum4 = character4.char_df.values.sum()
    sum5 = character5.char_df.values.sum()
    sum6 = character6.char_df.values.sum()

    word1.analyse_words(tokenlist1)  # Analyse the words for each text
    word2.analyse_words(tokenlist2)
    word3.analyse_words(tokenlist3)
    word4.analyse_words(tokenlist4)
    word5.analyse_words(tokenlist5)
    word6.analyse_words(tokenlist6)

    stop1 = word1.stop_word_frequency()  # Makes stop word frequency analysis for each text
    stop2 = word2.stop_word_frequency()
    stop3 = word3.stop_word_frequency()
    stop4 = word4.stop_word_frequency()
    stop5 = word5.stop_word_frequency()
    stop6 = word6.stop_word_frequency()

    stop1.columns = ['Number of occurence']   # Normally  stop_word_frequency method returns a Dataframe
    stop2.columns = ['Number of occurence']   # whose column name is Word Count but we will need to append the indexes
    stop3.columns = ['Number of occurence']   # different analysis. Therefore, we make the column names same such as
    stop4.columns = ['Number of occurence']   # 'Number of occurence' for each of analysis to append them easily.
    stop5.columns = ['Number of occurence']
    stop6.columns = ['Number of occurence']

    length1 = word1.get_word_length_frequency()  # Makes the word length analysis for each texts
    length2 = word2.get_word_length_frequency()
    length3 = word3.get_word_length_frequency()
    length4 = word4.get_word_length_frequency()
    length5 = word5.get_word_length_frequency()
    length6 = word6.get_word_length_frequency()

    length1.columns = ['Number of occurence']   # Same reason with   stop.columns = ['Number of occurence']
    length2.columns = ['Number of occurence']
    length3.columns = ['Number of occurence']
    length4.columns = ['Number of occurence']
    length5.columns = ['Number of occurence']
    length6.columns = ['Number of occurence']





    # Character Analyser includes number of occurrences of punctuation as well
    # Therefore, we just append the returning values of stop word analysis and
    # Word length analysis to character analysis to store all of 4 features needed
    # ( Character frequency, Punctuation frequency, Word length frequency, stop word frequency)


    character1.char_df = character1.char_df.append(stop1)
    character2.char_df = character2.char_df.append(stop2)
    character3.char_df = character3.char_df.append(stop3)
    character4.char_df = character4.char_df.append(stop4)
    character5.char_df = character5.char_df.append(stop5)
    character6.char_df = character6.char_df.append(stop6)

    character1.char_df = character1.char_df.append(length1)
    character2.char_df = character2.char_df.append(length2)
    character3.char_df = character3.char_df.append(length3)
    character4.char_df = character4.char_df.append(length4)
    character5.char_df = character5.char_df.append(length5)
    character6.char_df = character6.char_df.append(length6)

    character1.char_df.columns = ['File1']    # After appending all indexes and corresponding values
    character2.char_df.columns = ['File2']    # Renames the columns of each dataframe
    character3.char_df.columns = ['File3']
    character4.char_df.columns = ['File4']
    character5.char_df.columns = ['File5']
    character6.char_df.columns = ['File6']

    character1.char_df['File1'] = (character1.char_df['File1']) / sum1  # Frequencies are turned into relative frequencies by dividing total number of
    character2.char_df['File2'] = (character2.char_df['File2']) / sum2  # characters of each text
    character3.char_df['File3'] = (character3.char_df['File3']) / sum3
    character4.char_df['File4'] = (character4.char_df['File4']) / sum4
    character5.char_df['File5'] = (character5.char_df['File5']) / sum5
    character6.char_df['File6'] = (character6.char_df['File6']) / sum6



    # Stores 6 different DataFrame each storing analysis result of different texts into 1 using .concat() function.
    # It is needed because AnalysisVisualiser class needs an argument which is a Dataframe storing all the results of analysis done
    # in first 3 Tasks
    all_files_df = pd.concat([character1.char_df, character2.char_df, character3.char_df,
                              character4.char_df, character5.char_df, character6.char_df], axis=1, sort=False)

    all_files_df.fillna(0, inplace=True) # Beacuse there is un matching indexes for every 6 different dataframe
                                         # There are NaN values so this command replaces them with zero




    visiualise = Analysisvisualiser(all_files_df)

    visiualise.visualise_character_frequency()
    visiualise.visualise_punctuation_frequency()
    visiualise.visualise_stopword_frequency()
    visiualise.visualise_punctuation_frequency()

    all_files_df=all_files_df.round(5)   # Rounds the values to create a more readable format for user

    all_files_df.to_csv('All_data.txt', sep='\t', mode='a')     # Stores the content of Dataframe into a
                                                                # text file which will be created in the same folder with Python Project

if __name__ == '__main__':
    main()
