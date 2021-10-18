#!/usr/bin/env python3

def main():

    user_name = input("Enter username: ").title()
    day = input("Enter day of week: ").capitalize()
    #  print ("Hello, " + user_name + '! ' + "Happy " + day + '!')
 
    # format method
    #print("Hello, {}! Happy {}!".format(user_name,day))

    # f string
    #print(f"Hello, {user_name}! Happy {day}!"

    # with title method
    print(f"Hello, {user_name}! Happy {day}!")

main()
