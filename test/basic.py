import unittest
import requests
import sputnik

class BasicTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_number_of_results(self):
        requests_result = requests.get(
                'http://ws.spotify.com/search/1'
                '/track.json?q=nine+inch+nails+broken'
                ).json()
        sputnik_result = sputnik.search('nine inch nails broken')

        req_num_results = requests_result['info']['num_results']
        spu_num_results = sputnik_result['info']['num_results']

        self.assertEquals(req_num_results, spu_num_results,
                          "raw request and sputnik should return the same "
                          "number of results")

    def test_default_search_track(self):
        res = sputnik.search("echoplex")
        tracks = res.get("tracks")
        self.assertTrue(tracks is not None)

    def test_search_method_track(self):
        res = sputnik.search("the fragile", method="track")
        tracks = res.get("track")
        self.assertTrue(tracks is not None)

    def test_search_method_album(self):
        res = sputnik.search("the fragile", method="album")
        albums = res.get("albums")
        self.assertTrue(albums is not None)

    def test_search_method_artist(self):
        res = sputnik.search("david bowie", method="artist")
        artists = res.get("artists")
        self.assertTrue(artists is not None)


if __name__ == '__main__':
    unittest.main()
