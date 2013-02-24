from . import core


def search(terms, method='track'):
    if method != 'track' and method != 'album':
        raise ValueError("method should be 'track' or 'album'")
    return core.search(terms, method)
