import requests
import simplejson as json


def getbaseurl(service='search', version='1', method='track',
                format='json'):
    """Returns the base URL for a Spotify Web API query"""
    baseurl = "http://ws.spotify.com/{0}/{1}/{2}.{3}"
    return baseurl.format(service, version, method, format)


def search(terms, method='track'):
    if hasattr(terms, '__iter__'):
        sterms = ' '.join(terms)
    else:
        sterms = terms
    base = getbaseurl(method=method)
    r = requests.get(base, params={'q': sterms})
    if r.status_code != requests.codes.ok:
        raise NotImplementedException("There was some problem. Exception"
                "not defined yet")
    data = r.json()
    return data
