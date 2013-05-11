#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

# Imports
import random

# Getting all the questions
questions_file = open("questions_game2.txt", "r", encoding = "utf8")
questions = questions_file.readlines()
questions_file.close()

# The main method displaying questions
def main():
    # Keeping track of how many questions asked so far
    i = 1
    
    # Printing welcome-message
    print('Velkommen til Klubbas peke-på-spill!')
    print('')
    
    # Looping all the questions in random order
    while True:
        # Getting random question
        rnd = random.randrange(0, len(questions))
            
        # Printing
        print('Spm #'+str(i)+': '+questions[rnd].strip())
        
        # Waiting for next question
        foo = input()
        
        # Increasing question-number by one
        i += 1

# Calling the main-method! Let zhe gamez begin!
main()