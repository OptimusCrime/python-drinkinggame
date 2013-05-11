#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#
# Imports
#

import random

# Opening the file with all the questions
questions_file = open("questions_game1.txt", "r", encoding = "utf8")
questions = questions_file.readlines()
questions_file.close()

# Opening the file with the teams
teams_file = open("teams.txt", "r", encoding = "utf8")
teams_raw = teams_file.readlines()
teams_file.close()


def main():
    # Some need variables
    num_questions_each = 5
    current_question = 1
    current_team = 0
    teams = []
    
    # Printing welcome-message
    print('')
    print('==========================================')
    print('')
    print('Velkommen til Klubbas rygg-mot-rygg-spill!')
    print('')
    
    # Structuring teams in list
    for i in range(len(teams_raw)):
        # Splitting list on seperator
        teams_raw_split = teams_raw[i].split('|||')
        
        # Adding to the list
        teams.append(teams_raw_split[0].strip()+" og "+teams_raw_split[1].strip())
    
    # Getting number of questions pr. team
    while True:
        # Printing question
        print('Hvor mange spørsmål pr. gruppe? Det er '+str(len(teams))+' grupper.')
        
        # Getting response
        response = input('Antall spørsmål: ')
        
        # Validating if it is a number
        if (response.isnumeric()):
            if (int(response) > 0):
                num_questions_each = int(response)
                print('')
                break
        
        # Not valid input!
        print('')
        print('Ikke gyldig tallverdi. Prøv igjen')
        print('')
    
    # Let the games begin
    while True:
        print('==========================================')
        print('')
    
        # Printing info about current team
        print('Lag '+str(current_team+1)+': '+teams[current_team])
        print('')
        for i in range(1,(num_questions_each+1)):
            # Getting random question
            rnd = random.randrange(0, len(questions))
            
            # Printing
            print('Spm #'+str(i)+': '+questions[rnd].strip())
            
            # Waiting for next question
            foo = input()
        
        # Setting new team
        if ((current_team+1) >= len(teams)):
            current_team = 0
        else:
            current_team += 1
        

# Calling the main-method! Time to plaaayyy
main()