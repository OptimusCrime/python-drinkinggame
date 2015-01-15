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

# Opening the file with all the questions
questions_file = open('questions_game1.txt', 'r')
questions = questions_file.readlines()
questions_file.close()

# Opening the file with the teams
teams_file = open('teams.txt', 'r')
teams_raw = teams_file.readlines()
teams_file.close()

# Main method displaying the questions and everything 
def main():
    # Some need variables
    num_questions_each = 5
    current_question = 1
    current_team = 0
    teams = []
    
    # Structuring teams in list
    for i in range(len(teams_raw)):
        # Splitting list on seperator
        teams_raw_split = teams_raw[i].split('|||')
        
        # Adding to the list
        teams.append(teams_raw_split[0].strip() + ' og ' + teams_raw_split[1].strip())
    
    # Getting number of questions pr. team
    while True:
        # Printing question
        print '║                                   Hvor mange spørsmål pr. gruppe? Det er ' + bcolors.OKGREEN + str(len(teams)) + bcolors.ENDC + ' grupper.                                  ║'
        print '║                                                                                                                      ║'
        print '╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'
        print ''
        
        # Getting response
        response = str(raw_input(bcolors.OKGREEN + '> Antall spørsmål: ' + bcolors.ENDC))
        print ''

        # Validating if it is a number
        try:
            num = int(response)

            # It is a number, but is it valid?
            if num > 0:
                # We have outselvs a valid number!
                num_questions_each = num
                break
        except ValueError:
            pass
        
        # Not valid input!
        print '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'
        print '║                                                                                                                      ║'
        print '║                                           Ugyldig tallverdi. Prøv igjen.                                             ║'
        print '║                                                                                                                      ║'
        print '╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣'
        print '║                                                                                                                      ║'
    
    # Let the games begin
    while True:
        # Printing seprator
        print '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'
        print '║                                                                                                                      ║'
        
        # Printing info about current team
        temp_team = '║ Lag ' + str(current_team+1) + ': ' + teams[current_team]
        print '║ ' + bcolors.FAIL + 'Lag ' + str(current_team+1) + ': ' + bcolors.ENDC + teams[current_team] + repeat_to_length(' ', 119 - len(temp_team.decode('utf-8'))) + '║'
        print '║                                                                                                                      ║'
        print '╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣'
        foo = str(raw_input('║                                                                                                                      ║'))
        
        # Looping x number of questions pr. team
        for i in range(1, (num_questions_each+1)):
            # Getting random question
            rnd = random.randrange(0, len(questions))
            
            # Printing
            temp_question = '║ Spm #' + str(i) + ': ' + questions[rnd].strip()
            print '║ ' + bcolors.OKGREEN + 'Spm #' + str(i) + ': ' + bcolors.ENDC + questions[rnd].strip() + repeat_to_length(' ', 119 - len(temp_question.decode('utf-8'))) + '║'
            print '║                                                                                                                      ║'
            print '╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣'
            
            # Waiting for next question
            foo = str(raw_input('║                                                                                                                      ║'))
        
        # Setting new team
        if (current_team+1) >= len(teams):
            current_team = 0
        else:
            current_team += 1
        print '╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'
        print ''

# Calling the main-method! Time to plaaayyy
main()