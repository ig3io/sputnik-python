import requests
import simplejson as json


def getbaseurl(service='search', version='1', method='track',
                format='json'):
    """Returns the base URL for a Spotify Web API query"""
    baseurl = "http://ws.spotify.com/{0}/{1}/{2}.{3}"
    return baseurl.format(service, version, method, format)


class BaseSearch(object):
    def __init__(self, data):
        self.info = data['info']
        self.elements = None

    def __iter__(self):
        for el in self.elements:
            yield el


class TrackSearch(BaseSearch):
    def __init__(self, data):
        super(TrackSearch, self).__init__(data)
        self.elements = data['tracks']


class AlbumSearch(BaseSearch):
    def __init__(self, data):
        super(AlbumSearch, self).__init__(data)
        self.elements = data['albums']



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
    else:
        data = r.json()
        if method == 'track':
            return TrackSearch(data)
        elif method == 'album':
            return AlbumSearch(data)
        # There should be a check somewhere for method input!
