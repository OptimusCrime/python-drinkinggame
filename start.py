#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#
# Imports
#

import os

# Main-method
def main():
    # Introduction
    print('Hei og velkommen til klubbas drikkespill!')
    print('=========================================')
    print('')
    print('Velg hvilke spill dere ønsker å spille')
    print('')
    
    # Loop to make sure we have valid input
    while True:
        # Present the choices
        print('Skriv [p] for peke-leken eller [r] for rygg-mot-rygg-leken')
        
        # The the response
        response = input('Deres valg: ')
        
        # Make sure we have a valid reponse
        if (response == 'p' or response == 'r'):
            # Valid response
            
            # Print newline to clean up
            print('')
            print('=========================================')
            print('')
            
            # Find out what game we should call
            if (response == 'r'):
                # Rygg-mot-rygg - Calling teams.py to construct the teams
                os.system('python3 teams.py')
            else:
                # Peke - Calling game2. Let the games begin!
                 os.system('python3 game2.py')
            break
        else:
            # Not a valid response, provide feedback and continue the loop
            print('')
            print('Venligst prøv igjen...')
            print('')

# The the ball rolling here!
main()