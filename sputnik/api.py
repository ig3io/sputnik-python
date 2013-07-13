from . import core


def search(terms, method='track'):
    if method not in core.METHODS:
        raise ValueError("method should be 'track', 'album', or 'artist'")
    return core.search(terms, method)
