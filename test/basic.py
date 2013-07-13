import unittest
import requests
import sputnik


class BasicTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_number_of_results(self):
        requests_res = requests.get(
            'http://ws.spotify.com/search/1'
            '/track.json?q=nine+inch+nails+broken'
        ).json()
        sputnik_res = sputnik.search('nine inch nails broken')

        req_num = requests_res['info']['num_results']
        spu_num = sputnik_res['info']['num_results']

        self.assertEquals(req_num, spu_num, "raw request and sputnik should "
                          "return the same number of results")

    def test_default_search_track(self):
        res = sputnik.search("echoplex")
        tracks = res.get("tracks", None)
        self.assertTrue(tracks is not None)

    def test_search_method_track(self):
        res = sputnik.search("the fragile", method="track")
        tracks = res.get("tracks", None)
        self.assertTrue(tracks is not None)

    def test_search_method_album(self):
        res = sputnik.search("the fragile", method="album")
        albums = res.get("albums", None)
        self.assertTrue(albums is not None)

    def test_search_method_artist(self):
        res = sputnik.search("david bowie", method="artist")
        artists = res.get("artists", None)
        self.assertTrue(artists is not None)


if __name__ == '__main__':
    unittest.main()
