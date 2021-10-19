#!/usr/bin/env python3
""" Monty Python food recommendations """

def main():
    """ main """

    food  = ""
    count = 0

    while True:    
        ans = int(input("Please rate how hungry you are from 1 (not hungry) to 10 (very hungry): "))
        if ans < 1 or ans > 10:
            count = count + 1
            print ("please answer between 1 and 10")
            if count > 2: 
                print ("Three strikes, you're out")
                break
        else:
            if ans == 1:
                food = "a wafer thin mint"
            elif ans == 2:
                food = "lark's vomit"
            elif ans == 3:
                food = "an African sparrow"
            elif ans == 4:
                food = "a coconut"
            elif ans == 5: 
                food = "albatross"
            elif ans == 6:
                food = "chrunky frog"
            elif ans == 7:
                food = "the salmon mousse"
            elif ans == 8:
                food = "a dead parrot"
            elif ans == 9: 
                food = "an aquatic tart"
            elif ans == 10: 
                food = "spam, spam, spam..."
            print(f"food recommendation for hungry={ans} --->  {food}")
            break
main()
