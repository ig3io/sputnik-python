import unittest
import requests
import sputnik

class BasicTest(unittest.TestCase):

    def setUp(self):
        self.requests_result = requests.get(
                'http://ws.spotify.com/search/1'
                '/track.json?q=nine+inch+nails+broken'
                ).json()
        self.sputnik_result = sputnik.search('nine inch nails broken')


    def test_number_of_results(self):
        req_num_results = self.requests_result['info']['num_results']
        spu_num_results = self.sputnik_result['info']['num_results']
        self.assertEquals(req_num_results, spu_num_results,
                          "raw request and sputnik should return the same "
                          "number of results")


if __name__ == '__main__':
    unittest.main()
