#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

def main():
    #ipchk = "192.168.0.1"
    ipchk = input("Enter IP\n> ")

    # a string tests as True
    if ipchk:
        print("Looks like the IP address was set: " + ipchk)
    else: # if data is NOT provided
        print("No data provided.")
main()
