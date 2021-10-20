#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

# open file in read mode
#dnsfile = open("dnsservers.txt", "r")

with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep dnsfile open
    # loop accross lines in the file
    for svr in dnsfile:
        #print and end without newline
        print(svr, end="")

# no need to explicitly close file
