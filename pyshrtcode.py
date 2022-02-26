class shorten:
    import requests

    def shorten(url):
        response = shorten.requests.get('https://api.shrtco.de/v2/shorten?url=' + str(url)).json()
        return response

    def shrtcode(url):
        response = shorten.shorten(url)
        shortLink = response["result"]["full_short_link"]

        return shortLink

    def qrde(url):
        response = shorten.shorten(url)
        shortLink = response["result"]["full_short_link2"]

        return shortLink

    def shinyLink(url):
        response = shorten.shorten(url)
        shortLink = response["result"]["full_short_link3"]

        return shortLink
