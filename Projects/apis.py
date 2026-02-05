# https://api.artic.edu/api/v1/artworks/search

import requests
import json

def main():

    print('Search the Art Inst. of Chichago!!')
    name = input("Enter the artist's name whose work you wanna see: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {'q': name}
        )
    # print(response.json())
    except requests.HTTPError:
        print("Couldn't complete request")

    # content = json.dumps(response.json(), indent= 2)
    content = response.json()
    # print(content)

    for artworks in content['data']:
        print(artworks['title'])

main()