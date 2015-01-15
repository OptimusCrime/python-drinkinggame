#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Imports
import random

# For colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

# Generate x spaces
def repeat_to_length(string_to_expand, length):
   return (string_to_expand * int((length/len(string_to_expand))+1))[:length]

# Getting all the questions
questions_file = open('questions_game2.txt', 'r')
questions = questions_file.readlines()
questions_file.close()

# The main method displaying questions
def main():
    # Keeping track of how many questions asked so far
    i = 1
    
    # Printing welcome-message
    print ''
    print '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'
    print '║                                                                                                                      ║'
    print '║                                                ' + bcolors.OKGREEN + 'Klubbas Peke-På-Spill!' + bcolors.ENDC + '                                                ║'
    print '║                                                                                                                      ║'
    print '╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'
    print ''
    
    print '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'
    print '║                                                                                                                      ║'
    
    # Looping all the questions in random order
    while True:
        # Getting random question
        rnd = random.randrange(0, len(questions))
        
        question_string = '║ Spm #' + str(i) + ': ' + questions[rnd].strip()
        question_whitespace = 119 - len(question_string.decode('utf-8'))
        
        # Printing
        print '║ ' + bcolors.OKGREEN + 'Spm #' + str(i) + ': ' + bcolors.ENDC + questions[rnd].strip() + repeat_to_length(' ', question_whitespace) + '║'
        print '║                                                                                                                      ║'
        print '╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣'
        
        # Waiting for next question
        foo = str(raw_input('║                                                                                                                      ║'))
        
        # Increasing question-number by one
        i += 1

# Calling the main-method! Let zhe gamez begin!
main()