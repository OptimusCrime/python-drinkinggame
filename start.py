#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Imports
import os

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

# Main-method
def main():
    # Printing introduction
    print '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'
    print '║                                                                                                                      ║'
    print '║                                      ' + bcolors.OKGREEN + 'Hei og velkommen til klubbas drikkespill!' + bcolors.ENDC + '                                       ║'
    print '║                                                                                                                      ║'
    print '╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'
    print ''
    print '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'
    print '║                                                                                                                      ║'
    print '║                                        Velg hvilke spill dere ønsker å spille                                        ║'
    print '║                                                                                                                      ║'
    # Loop to make sure we have valid input
    while True:
        # Present the choices
        print '╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣'
        print '║                                                                                                                      ║'
        print '║                              Skriv ' + bcolors.FAIL + '[p]' + bcolors.ENDC + ' for peke-leken eller ' + bcolors.FAIL + '[r]' + bcolors.ENDC + ' for rygg-mot-rygg-leken                              ║'
        print '║                                                                                                                      ║'
        print '╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝'
        print ''
        
        # The the response
        response = str(raw_input(bcolors.OKGREEN + '> Deres valg: ' + bcolors.ENDC))
        
        # Make sure we have a valid reponse
        if response == 'p' or response == 'r':
            # We have a valid response! Find out what game we should call       
            if response == 'r':
                # Rygg-mot-rygg - Calling teams.py to construct the teams
                os.system('python teams.py')
            else:
                # Peke - Calling game2. Let the games begin!
                 os.system('python game2.py')
            break
        else:
            # Not a valid response, provide feedback and continue the loop
            print ''
            print '╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗'
            print '║                                                                                                                      ║'
            print '║                                                Vennligst prøv igjen                                                  ║'
            print '║                                                                                                                      ║'

# The the ball rolling here!
main()