from random import * 
from funkload.FunkLoadTestCase import FunkLoadTestCase
import urllib2,json
import httplib
from dateutil.parser import parse
from decimal import *

LAT_CENTR = 37.765
LON_CENTR = -122.403
class LoadTest(FunkLoadTestCase):

    def setUp(self):

        self.server_url = self.conf_get('main', 'url')


    def test_postget(self):
        print "basic post and get"
        server_url = self.server_url 
        url = server_url+'/'
        i = 17
        data = {"status" : "APPROVED",\
          "expirationdate" : "2015-03-15T00:00:00",\
          "permit" : "14MFF-0107",\
          "block" : "3794",\
          "received" : "Jun 24 2014  1:49PM",\
          "facilitytype" : "Truck",\
          "blocklot" : "3794002A",\
          "locationdescription" : "02ND ST: TOWNSEND ST to KING ST (700 - 799)",\
          "cnn" : 148000,\
          "priorpermit" : 1,\
          "approved" : "2014-06-24T13:55:30",\
          "noisent" : "2013-07-25T00:00:00",\
          "schedule" : "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=14MFF-0107&ExportPDF=1&Filename=14MFF-0107_schedule.pdf",\
          "address" : "750 02ND ST",\
          "applicant" : "Steve's Mobile Deli",\
          "lot" : "002A",\
          "fooditems" : "Cold Truck: Pre-packaged sandwiches: Burgers: Hot Dogs: Muffin Sandwiches: Enchiladas: Bagels: Burritos: Salads: Snacks: Beverages",\
          "longitude" : -122.402978526686,\
          "latitude" : 37.7302216813049, \
          "y" : 2093947.369,\
          "x" : 6011371.493,\
          "objectid" : i}
        
        req = urllib2.Request(url )
        req.add_header('Content-Type','application/json')
        postdata = json.dumps(data)
        #req.get_method = lambda: 'DELETE'
        res = urllib2.urlopen(req, postdata)
        self.assertEqual(res.code, 201)
        response = json.loads(res.read())
        quant = '1.000000'
        for k, v in data.iteritems():
           
            if v is not None and (k is "y" or k is "x" or k is "latitude" or k is "longitude"):
                self.assertEqual(Decimal(response[k]).quantize(Decimal(quant)), Decimal(v).quantize(Decimal(quant)))
            elif v is not None and (k is "approved" or k is "received" or k is "expirationdate" or k is "noisent"):
                self.assertEqual(parse(response[k]), parse(v))
            else:
                self.assertEqual(response[k], v)
        
        req = urllib2.Request(url+ str(i))
        res = urllib2.urlopen(req)
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        for k, v in data.iteritems():
            if v is not None and (k is "y" or k is "x" or k is "latitude" or k is "longitude"):
                self.assertEqual(Decimal(response[k]).quantize(Decimal(quant)), Decimal(v).quantize(Decimal(quant)))
            elif v is not None and (k is "approved" or k is "received" or k is "expirationdate" or k is "noisent"):
                self.assertEqual(parse(response[k]), parse(v))
            else:
                self.assertEqual(response[k], v)
        req = urllib2.Request(url + str(i) )
        req.add_header('Content-Type','application/json')
        req.get_method = lambda: 'DELETE'
        res = urllib2.urlopen(req)
        print 'pass'

    def test_searchByID(self):
        print 'Test searchByID: GET, PUT, DELETE'
        """POST"""
        server_url = self.server_url 
        url = server_url+'/'
        data = { "objectid" : 1, "x": 1.0, 'y': 1.5}
        
        req = urllib2.Request(url)
        req.add_header('Content-Type','application/json')
        postdata = json.dumps(data)
        res = urllib2.urlopen(req, postdata)
        """GET"""
        url = url + '1'
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        self.assertEqual(response['objectid'], 1)
        self.assertEqual(float(response['x']), 1.0)
        self.assertEqual(float(response['y']), 1.5)

        """PUT"""
        data = {'objectid': 1, 'x': 1.0, 'y': 2.0}
        req = urllib2.Request(url)
        req.add_header('Content-Type','application/json')
        req.get_method = lambda: 'PUT'
        postdata = json.dumps(data)
        res = urllib2.urlopen(req, postdata)
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        self.assertEqual(response['objectid'], 1)
        self.assertEqual(float(response['x']), 1.0)
        self.assertEqual(float(response['y']), 2.0)
        """DELETE"""
        
        self.assertEqual(self.delete_id(1).code, 204)
        print 'pass'

    def test_searchByKeyword(self):
        """
        Test retrieving foodtruck record by keyword
        """

        print 'Test: retrieving foodtruck record by keyword'
        server_url = self.server_url 
        
        s0 = str(random())
        data0 = {'objectid': 3, 'applicant':s0, 'x': 0.0, 'y': 0.5}
        data1 = {'objectid': 4, 'applicant':'Chicago', 'fooditems': 'deep dish %s and sandwiches' %s0, 'x': 1.0, 'y': 1.0}
        data2 = {'objectid': 5, 'applicant':'hotdog', 'x': 1.5, 'y': 1.5}
        
        res = self.post_data(data0)
        res = self.post_data(data1)
        res = self.post_data(data2)

        url = server_url + '/bykeyword?keyword=%s' %s0
        res = self.get_url(url)
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['objectid'], 3)
        self.assertEqual(response[1]['objectid'], 4)
        
        
        self.delete_id(3)
        self.delete_id(4)
        self.delete_id(5)

        print 'pass'

    def test_searchByLocation(self):
        """
        Test retrieving  foodtrucks nearby
        """
        print 'Test: retrieving  foodtrucks nearby'
        server_url = self.server_url 
        data = [{'objectid': 0,  'latitude':37.7841781516735  , 'longitude':-12.394064145441 },\
                {'objectid': 1,  'latitude':37.7862060821039  , 'longitude':-12.402532491346 },    #ft2 is closest to ft0\
                {'objectid': 2,  'latitude':37.7800057026855  , 'longitude':-12.390270961311 },    #ft1 is further to ft0\
                {'objectid': 3,  'latitude':32  , 'longitude': -100}]                               #ft3 is far far away
        for d in data:
            response = self.post_data(d)
            self.assertEqual(response.code, 201)
        
        lat = data[0]['latitude']   #given latitude
        lon = data[0]['longitude']  #given longitude
        rad = 3                     #given radius of search
        lim = 2 

        """ test both urls: w/ or w/out limit """
        res = self.get_url(server_url+'/bylocation?latitude=%f&longitude=%f&radius=%f' % (lat, lon, rad))
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        self.assertEqual(len(response), 3)
        self.assertEqual(response[0]['objectid'], 0)
        self.assertEqual(response[1]['objectid'], 2)       
        self.assertEqual(response[2]['objectid'], 1)       

        res = self.get_url(server_url+'/bylocation?latitude=%f&longitude=%f' % (lat, lon))
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        self.assertEqual(len(response), 3)
        
        res = self.get_url(server_url+'/bylocation?latitude=%f&longitude=%f&radius=%f&limit=%d' % (lat, lon, rad, lim))
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        self.assertEqual(len(response), 2)
        
        """ test the radius: shrink the radius such that only ft0 will be found """
        rad = 0.01
        res = self.get_url(server_url+'/bylocation?latitude=%f&longitude=%f&radius=%f' % (lat, lon, rad))
        response = json.loads(res.read())
        self.assertEqual(res.code, 200)
        self.assertEqual(len(response), 1)

        self.delete_id(0)
        self.delete_id(1)
        self.delete_id(2)
        self.delete_id(3)
        print 'pass'

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
    
    def get_url(self, url):
        req = urllib2.Request(url )
        res = urllib2.urlopen(req)
        return res

    def delete_id(self, i):
        url = self.server_url + "/" + str(i)
        req = urllib2.Request(url )
        req.get_method = lambda: 'DELETE'
        res = urllib2.urlopen(req)
        return res

    def post_data(self, data):
        url = self.server_url+'/'
        req = urllib2.Request(url)
        req.add_header('Content-Type','application/json')
        postdata = json.dumps(data)
        res = urllib2.urlopen(req, postdata)
        return res

if __name__ in ('main', '__main__'):

    unittest.main()
