import requests


class UrlShortener:
    def __init__(self, api_key, domain):
        firebase_api_url = (
            'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={}')
        self.api_url = firebase_api_url.format(api_key)
        self.domain = domain

    def get_short_link(self, long_url):
        url = "https://{}.page.link/?link={}&apn=com.{}.android&ibi=com.{}.ios"

        long_dynamic_link = url.format(
            self.domain, long_url, self.domain, self.domain)

        payload = {
            "longDynamicLink": long_dynamic_link
        }
        response = requests.post(self.api_url, json=payload)
        json_data = response.json()

        if response.status_code != 200:
            return json_data

        return json_data.get('shortLink')
