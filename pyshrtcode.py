class short:
    import requests

    def shorten(url):
        response = short.requests.get('https://api.shrtco.de/v2/shorten?url=' + url).json()
        
        shortLink1 = response["result"]["full_short_link"]
        shortLink2 = response["result"]["full_short_link2"]
        shortLink3 = response["result"]["full_short_link3"]

        return shortLink1, shortLink2, shortLink3