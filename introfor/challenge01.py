#!/usr/bin/env python3



def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
#        print(farm)
        print(farm.get("name", "Unknown Farm"), end=":\n")
        for ag in farm.get("agriculture"):
            print ("  -", ag)
main()


