# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 12:37:19 2016

@author: CAMHW5
"""
import random
    
def read_from_file_to_list(filename):
    words_list = []
    file_to_open = open(filename)
    for line in file_to_open:
        word = line.strip()
        words_list.append(word)
    return words_list

def airport_novel_generator():
    ''' Generates the name of a Da Vinci Code type mystery novel you might pick up in an airport
    eg "The Perseus Plot" and returns it '''
    
    #make a list of first words - mythological figures, planets etc
    first_words_list = read_from_file_to_list('first_airport_novel_words.txt')
    #make a list of second words - exciting ones like 'Conspiracy'
    second_words_list = read_from_file_to_list('second_airport_novel_words.txt')
    
    #generate the title randomly
    airport_novel_title = "The %s %s" % (random.choice(first_words_list), random.choice(second_words_list))
    return airport_novel_title
    
def main():
    print airport_novel_generator()

if __name__ == "__main__":
    main() #only run if it's the main script
