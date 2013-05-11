#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#
# Imports
#

import random
import os

# All the existing names
names = open("names.txt", "r", encoding = "utf8")
names_lines = names.readlines()

# The main-method
def main():
    # If we actually have some players
    if (len(names_lines) > 0):
        # Print to ask
        print('Spill med eksisterende spillere?')
        
        # Loop the array to display what players we have from before
        names_arr = []
        for i in range(0,len(names_lines)):
            names_arr.append(names_lines[i].strip())
        
        # Display the names
        print('Spillere: '+', '.join(names_arr)+' ['+str(len(names_arr))+']')
        print('')
        
        # Loop to make the instructions appear several times
        while True:
            # Displaying intructions
            if (len(names_lines) % 2 == 0):
                print('Skriv [y] for å bruke spillerne, [a] for å legge til nye navn eller [n] for å opprette ny liste.')
            else:
                print('Skriv [a] for å legge til nye navn eller [n] for å opprette ny liste.')
            
            # Response
            response = input('Ditt svar: ')
            
            # Validating the response
            if ((response == 'y' and (len(names_lines) % 2 == 0)) or response == 'a' or response == 'n'):
                # Valid response
                if (response == 'y'):
                    # Using the old list
                    generate_team()
                elif (response == 'a'):
                    # Appending new names
                    varrrr = 1
                else:
                    # Totally new list
                    varrrr = 1
                break
            else:
                # Not a valid response, provide feedback and continue the loop
                print('')
                print('Venligst prøv igjen…')
                print('')

# Method to generate the teams based on the names we have in the file right now
def generate_team():
    i = 0
    lagNr = 1
    linje = ""
    while len(lag) > 0:
        if len(lag) == 1:
            rand = 0
        else:
            rand = random.randrange(0,len(lag)-1)
        
        if i % 2 != 0:
            print("Lag "+str(lagNr)+" er: "+linje+" og "+lag[rand])
            lagNr += 1
        else:
            linje = lag[rand]
            lag.pop(rand)
        i += 1

# Method to append names to the file
def append_names():
    # TODO
    varrrr = 1

# Method to add new names to the file
def new_names():
    # TODO
    varrrr = 1


# Calling the main-method!
main()