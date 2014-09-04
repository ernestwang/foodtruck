from random import * 
from funkload.FunkLoadTestCase import FunkLoadTestCase

LAT_CENTR = 37.765
LON_CENTR = -122.403
class LoadTest(FunkLoadTestCase):

    def setUp(self):

        self.server_url = self.conf_get('main', 'url')

    def test_load(self):
    	seed()
    	latitude = LAT_CENTR + 0.1 * (random()  - 0.5)
    	longitude = LON_CENTR + 0.1 * (random() - 0.5)
    	radius = uniform(0,10)
    	limit = randint(1,100)
        server_url = self.server_url + "/bylocation?latitude=%f&longitude=%f&radius=%f&limit=%d" \
        							% (latitude, longitude, radius, limit)
        res = self.get(server_url, description='Get url')

        self.assertEqual(res.code, 200)


if __name__ in ('main', '__main__'):

    unittest.main()
