#!/usr/bin/env python3

import pandas as pd

def main():
    poke_df= pd.read_csv("pokedext.txt")
    print(poke_df.head(10))

main()
