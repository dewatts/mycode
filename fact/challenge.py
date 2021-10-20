#!/usr/bin/env python3
"""Alta3 Research | RZFeeser Old MacDonalds Farm """

def function1( my_farm ):
    print ("i'm in the f1")
    print ( my_farm.get("NE Farm"))

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        print("checking if farm is NE")
        print (farm)

#        print( farm.keys() )
#        print( farm.values() )

        if  farm["name"] == "NE Farm":
            print :wq


main()
