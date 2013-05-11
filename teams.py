#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

# Imports
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
        # Print to ask question
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
            # Displaying different intructions depending on if the game can start now or not
            if (len(names_lines) % 2 == 0):
                print('Skriv [y] for å bruke spillerne, [a] for å legge til nye navn eller [n] for å opprette ny liste.')
            else:
                print('Skriv [a] for å legge til nye navn eller [n] for å opprette ny liste.')
            
            # Catching the response
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
                    print('Legg til navn i lista. Begynn spillet ved å skrive [p].')
                    print('')
                    
                    # Calling the method
                    new_names()
                break
            else:
                # Not a valid response, provide feedback and continue the loop
                print('')
                print('Venligst prøv igjen...')
                print('')

# Method to generate the teams based on the names we have in the file right now
def generate_team():
    # Printing information
    print('')
    print('Lagene er som følger:')
    print('')
    
    # Some variables we need
    i = 0
    team_number = 1
    other = ""
    
    # Cleaning the file with existing teams
    open('teams.txt', 'w').close()
    
    # Opening the file with all the names
    names = open("names.txt", "r", encoding = "utf8")
    names_lines = names.readlines()
    names.close()
    
    # Looping all the names
    while len(names_lines) > 0:
        # If we only have one name left, it's the 0-index. If not, chose a random index
        if len(names_lines) == 1:
            rand = 0
        else:
            rand = random.randrange(0,len(names_lines)-1)
        
        # Every second line should output and store the team-info
        if i % 2 != 0:
            # Outputting the information
            print("Lag "+str(team_number)+": "+other+" og "+names_lines[rand].strip())
            
            # Storing the informasion in the teams-file
            with open("teams.txt", "a") as myfile:
                myfile.write(other+'|||'+names_lines[rand].strip()+'\n')
                myfile.close()
            
            # Increase the team number by one
            team_number += 1
        else:
            # Adding the name
            other = names_lines[rand].strip()
        
        # Removing the name from the line
        names_lines.pop(rand)
        
        # Increasing the index to keep track of even/odd-events
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
            # Getting all existing names from the file
            names = open("names.txt", "r", encoding = "utf8")
            names_lines = names.readlines()
            names.close()
            
            # Checking even/odd
            if (len(names_lines) % 2 == 0):
                # Even number, lets generate some teams!
                generate_team()
                break
            else:
                # Odd number, can't start playing yet
                print('')
                print('Beklager, lagene må gå opp i to. Dere har '+str(len(names_lines))+' navn. Legg til en til!')
                print('')
        else:
            # Adding name, check to see if duplicate
            names = open("names.txt", "r", encoding = "utf8")
            names_lines = names.readlines()
            names.close()
            
            # Keeping track if we found the name in the file or not
            names_contains_name = False
            
            # Checking for duplicates in the list
            for i in range(len(names_lines)):
                if (names_lines[i].strip().lower() == name.lower()):
                    # This name is a duplicate
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