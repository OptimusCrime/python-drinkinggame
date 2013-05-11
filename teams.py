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
names.close()

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
                    # Using the old list. Calling the method
                    generate_team()
                elif (response == 'a'):
                    # Appending new names to the list. Printing instructions
                    print('')
                    print('Legg til nye navn i lista. Begynn spillet ved å skrive [p].')
                    print('')
                    
                    # Calling method
                    append_names()
                else:
                    # Making a new list. Printing instructions
                    print('')
                    print('Legg til nye navn i lista. Begynn spillet ved å skrive [p].')
                    print('')
                    
                    # Calling the method
                    new_names()
                break
            else:
                # Not a valid response, provide feedback and continue the loop
                print('')
                print('Venligst prøv igjen…')
                print('')

# Method to generate the teams based on the names we have in the file right now
def generate_team():
    # Printing instructions
    print('')
    print('Lagene er som følger:')
    print('')
    
    # Some lines
    i = 0
    lagNr = 1
    linje = ""
    
    # Cleaning the file with existing teams
    # First removing all the content in the file
    open('teams.txt', 'w').close()
    
    # Opening the file with all the names
    names = open("names.txt", "r", encoding = "utf8")
    names_lines = names.readlines()
    names.close()
    
    # Looping all the names
    while len(names_lines) > 0:
        if len(names_lines) == 1:
            rand = 0
        else:
            rand = random.randrange(0,len(names_lines)-1)
        
        if i % 2 != 0:
            print("Lag "+str(lagNr)+": "+linje+" og "+names_lines[rand].strip())
            lagNr += 1
        else:
            linje = names_lines[rand].strip()
        
        names_lines.pop(rand)
        i += 1
    
    # Let's play!
    os.system('python3 game1.py')

# Method to append names to the file
def append_names():
    # Looping 'till done
    while True:
        # Getting response
        name = input('Navn: ')
        
        # Checking if adding or quitting
        if (name == 'p'):
            # Trying to quit. Do we have an even number of teams?
            names = open("names.txt", "r", encoding = "utf8")
            names_lines = names.readlines()
            names.close()
            
            # Checking even/odd
            if (len(names_lines) % 2 == 0):
                # Even number, lets generate some teams!
                generate_team()
                break
            else:
                print('')
                print('Beklager, lagene må gå opp i to. Dere har '+str(len(names_lines))+' navn. Legg til en til!')
                print('')
        else:
            # Adding name, check to see if duplicate
            names = open("names.txt", "r", encoding = "utf8")
            names_lines = names.readlines()
            names.close()
            
            names_contains_name = False
            
            # Checking for duplicates in the list
            for i in range(len(names_lines)):
                if (names_lines[i].strip().lower() == name.lower()):
                    # Duplicate
                    names_contains_name = True
                    break
            
            # Checking result from loop above
            if (names_contains_name):
                # We have ourselvs a duplicate!
                print('Navnet finnes i listen fra før!')
            else:
                # We have no duplicates in here! Append name to file
                with open("names.txt", "a") as myfile:
                    myfile.write(name+'\n')
                    myfile.close()

# Method to add new names to the file
def new_names():
    # First removing all the content in the file
    open('names.txt', 'w').close()
    
    # Call method to add new names
    append_names()


# Calling the main-method!
main()