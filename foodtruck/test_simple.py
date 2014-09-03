from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase

LAT_CENTR = 37.765
LON_CENTR = -122.403
class LoadTest(FunkLoadTestCase):

    def setUp(self):

        self.server_url = self.conf_get('main', 'url')

    def test_simple(self):
    	random.seed()
    	latitude = LAT_CENTR + 0.1 * (random.random() * 2 - 1.0)
    	longitude = LON_CENTR + 0.1 * (random.random() * 2 - 1.0)
    	radius = random.uniform(0,10)
    	limit = random.randint(1,100)
        server_url = self.server_url

        res = self.get(server_url + "/bylocation?latitude=%f&longitude=%f&radius=%f&limit=%d" \
        							% (latitude, longitude, radius, limit), description='Get url')

        self.assertEqual(res.code, 200)


if __name__ in ('main', '__main__'):

    unittest.main()
