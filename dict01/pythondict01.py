#!/usr/bin/env python3

def main():

    ## create a dictionary
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display parts of the dictionary
    print( switch["hostname"] )
    print( switch["ip"] )

    ## request a 'fake' key
#    print( switch["lynx"] )

    ## request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get("lynx") )

    print( "Second test - .get()" )
    print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

    print( "Third test - .get()" )
    print( switch.get("version") )

    print( "Fourth test - .keys()" )
    print( switch.keys() )

    print( "Fifth test - .values()" )
    print( switch.values() )

    print( "Six test - .pop()" )
    switch.pop("version")   # remoes this key (and value) pair
    print( switch.keys() )  # notice the value of version is gone
    print( switch.values() ) # notice the value of 1.2

    print( "Seventh test - ADD a new value" )
    switch["adminlogin"] = "karl08"
    print( switch.keys() )
    print( switch.values() )

    print( "Eighth test - ADD a new value" )
    switch["password"] = "qwerty"
    print( switch.keys() )
    print( switch.values() )

    print( "Ninth test - popitem")
    switch.popitem()
    print( switch.keys() )
    print( switch.values() )

    print( "Tenth test - Another popitem")
    switch.popitem()
    print( switch.keys() )
    print( switch.values() )

main()
