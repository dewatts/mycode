#!/usr/bin/env python3
""" this is my docstring """

def main():
    """ main docstring """

    # Obtain hostname value
    hostname = input("What value should we set for hostname?")

    ## here we use the str.lower() method to return a lowercase string
    if hostname == "mtg":
        print("The hostname was found to be mtg")
        print("Hostname matches expected config")

    # print exit string
    print("Exiting the script.")

main()
