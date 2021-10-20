#!/usr/bin/env python3
""" Monty Python food recommendations """

def main():
    """ main """

#    responses= {"1":"a wafer thin mint",
#                "2":"lark's vomit",
#                "3":"an African sparrow",
#                "4":"a coconut",
#                "5":"albatross",
#                "6":"chrunky frog",
#                "7":"the salmon mousse",
#                "8":"a dead parrot",
#                "9":"an aquatic tart",
#                "10":"spam, spam, spam..."
#                }
#

    inf = open('pyfood.dict','r')
    responses = eval(inf.read())
    inf.close()


    while True:    
        choice = input("Please rate how hungry you are from 1 (not hungry) to 10 (very hungry): ")
        if choice.lower() == "q":
            break
        msg= responses.get(choice)
        if msg:
            print(msg)
        else:
            print("Choose a number between 1 and 10.")
main()
