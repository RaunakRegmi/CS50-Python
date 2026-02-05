# https://api.artic.edu/api/v1/artworks/search
# import requests
# import json
# from artwork import art_works

from museum.artwork import art_works

def main():
    # Asks for artwork to see, prints artwork formatting
    artwork = input("Artwork: ")
    limit = input("Limit you wanna see: ")

    artworks = art_works(query=artwork, limit=limit)
    for works in artworks:
        print(works)

main()
