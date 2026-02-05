# https://api.artic.edu/api/v1/artworks/search
# import requests
# import json
# from artwork import art_works

from museum.artwork import art_works
from museum.artist import artists

def main():
    # Asks for artwork to see, prints artwork formatting
    artists = input("Artists: ")
    limit = input("Limit you wanna see: ")

    artists = art_works(query=artists, limit=limit)
    for works in artists:
        print(works)

main()
