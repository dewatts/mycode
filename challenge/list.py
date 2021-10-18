#!/usr/bin/env python3

def main():
    icecream= ["flavors", "salty"]
    northerntrust= ["Alex","Andrew","Dave","Julia","Kurt","Marlon","Roger","Seth","Tim","Viq"]

    icecream.append(99)

    print (icecream)

    uindex = int(input ("Enter a 0 and 9 to select user: \n>"))
    iindex = int(input ("Enter a 0 or 1 too select icecream: \n>"))

    #print (icecream[-1])
    #print (northerntrust[uindex])
    #print (icecream[iindex])

    print (f"{icecream[-1]} {icecream[0]}, and {northerntrust[uindex]} chooses to be {icecream[iindex]} ")

main()





