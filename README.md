# Firebase Dynamic Links URL Shortener 

This is a Python Client for Firebase Dynamic Links to Create Short URLs.

## Requirements

Be sure you have the following installed on your development machine:

+ Python >= 3.6.3
+ requests


## Usage

```python
from url_shortener.url_shortener import UrlShortener

url_shortener = UrlShortener('your_api_key', 'domain_name')
url_shortener.get_short_link('https://www.example.com/')
```

## Note
Here Domain Name Refers to The Subdomain you set for your Dynamic Links.