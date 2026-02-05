# https://api.artic.edu/api/v1/artworks/search
import requests


def artists(query, limit):

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()

    except requests.HTTPError:
        print('Something went wrong')
        return []

    content = response.json()

    return [works['title'] for works in content['data']]