#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description: ISS

   """

# imports always go at the top of your code
import requests

def main():
    """Run time code"""

    API="http://api.open-notify.org/iss-now.json"
    # create resp, which is our request object
    resp = requests.get(API)

    # display the methods available to our new object
    print( resp.json().keys())


    position = resp.json().get("iss_position")
    longitude=position.get('longitude')
    latitude=position.get('latitude')

#    longitude=["longitude"]
    
    print("Current LOCATION OF THE ISS:")
    print (longitude)
    print (latitude)

    #print(f"Lon: {resp.json(['longitude'])}")
    #print(f"Lat: {resp.json(['latitude'])}")

if __name__ == "__main__":
    main()

