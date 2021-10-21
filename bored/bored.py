#! /usr/bin/env python3
""" Python Training | Author: Dave Watts """

# import always goes to top of code
import requests

API = " http://www.boredapi.com/api/activity/"

def main():

    activities={"education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"}


    # Create resp, which is our request object
    # randon activity
    resp = requests.get(f"{API}")
    print ("Random Activity")
    print ( resp.json() )
    print ()

    for activity in activities:
        resp = requests.get(f"{API}?type={activity}")
        print (f"{activity} Activity")
        print ( resp.json() )
        print ()

main()
