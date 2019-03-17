import unittest

from url_shortener import UrlShortener


class TestUrlShortener(unittest.TestCase):

    def setUp(self):
        self.domain = 'test'
        self.api_key = 'test123'
        self.shorten_url = UrlShortener(self.api_key, self.domain)

    def test_api_url(self):
        self.assertEqual(
            self.shorten_url.api_url,
            'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={}'
            .format(self.api_key))

    def test_get_short_link_with_no_argument(self):
        with self.assertRaises(TypeError):
            self.shorten_url.get_short_link()

    def test_get_short_link(self):
            response = self.shorten_url.get_short_link('www.google.com')

            self.assertEqual(response['error']['code'], 400)
            self.assertEqual(
                response['error']['message'],
                'API key not valid. Please pass a valid API key.')


if __name__ == '__main__':
    unittest.main()
