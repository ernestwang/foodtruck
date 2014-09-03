======================
FunkLoad_ bench report
======================


:date: 2014-09-03 10:47:59
:abstract: Simple demo
           Bench result of ``Simple.test_simple``: 
           Access our Demo app

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2014-09-03 10:47:59
* From: erzhuos-MacBook.local
* Test: ``test_simple.py Simple.test_simple``
* Target server: http://localhost:8000
* Cycles of concurrent users: [5, 10, 100]
* Cycle duration: 60s
* Sleeptime between request: from 0.0s to 0.5s
* Sleeptime between test case: 0.01s
* Startup delay between thread: 0.001s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.16.1


Bench content
-------------

The test ``Simple.test_simple`` contains: 

* 1 page(s)
* 0 redirect(s)
* 0 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 9820 tests, 1367 error(s)
* 9838 pages, 1367 error(s)
* 9838 requests, 1367 error(s)


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  5             18.517               1111               1111             0.00%
                 10             35.367               2122               2122             0.00%
                100             87.000               6587               5220            20.75%
 ================== ================== ================== ================== ==================



Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  5              1.000          Excellent             18.583             26.000               1115               1115             0.00%              0.007              0.012              0.043              0.008              0.010              0.018              0.021
                 10              1.000          Excellent             35.517             45.000               2131               2131             0.00%              0.007              0.016              0.091              0.009              0.012              0.028              0.037
                100              0.945          Excellent             87.083            104.000               6592               5225            20.74%              0.042              0.403             19.284              0.145              0.214              1.206              2.182
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Request stats
-------------

The number of **Requests** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*            Rating*                RPS             maxRPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  5              1.000          Excellent             18.583             26.000               1115               1115             0.00%              0.007              0.012              0.043              0.008              0.010              0.018              0.021
                 10              1.000          Excellent             35.517             45.000               2131               2131             0.00%              0.007              0.016              0.091              0.009              0.012              0.028              0.037
                100              0.945          Excellent            109.867            129.000               6592               5225            20.74%              0.001              0.688             19.284              0.152              0.236              1.954              2.226
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **100** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.69s, get: ``http://localhost:8000``
  `Get url`

Page detail stats
-----------------


PAGE 001: Get url
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ````

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      5              1.000          Excellent               1115               1115             0.00%              0.007              0.012              0.043              0.008              0.010              0.018              0.021
                     10              1.000          Excellent               2131               2131             0.00%              0.007              0.016              0.091              0.009              0.012              0.028              0.037
                    100              0.945          Excellent               6592               5225            20.74%              0.001              0.688             19.284              0.152              0.236              1.954              2.226
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

Failures and Errors
-------------------


Errors
~~~~~~

* 1367 time(s), code: -1::

    Traceback (most recent call last):
   
    File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/funkload/FunkLoadTestCase.py", line 202, in _connect
    cert_file=self._certfile_path, method=rtype)
   
    File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/funkload/PatchWebunit.py", line 360, in WF_fetch
    h.endheaders()
   
    File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 954, in endheaders
    self._send_output(message_body)
   
    File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 814, in _send_output
    self.send(msg)
   
    File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 776, in send
    self.connect()
   
    File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 757, in connect
    self.timeout, self.source_address)
   
    File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 571, in create_connection
    raise err
 error: [Errno 61] Connection refused



Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/xmlrpc request.
* Page: a request with redirects and resource links (image, css, js) for an html page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second, successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: 10th percentile, response time where 10 percent of pages or requests are delivered.
* MED: Median or 50th percentile, response time where half of pages or requests are delivered.
* P90: 90th percentile, response time where 90 percent of pages or requests are delivered.
* P95: 95th percentile, response time where 95 percent of pages or requests are delivered.
* Apdex T: Application Performance Index, 
  this is a numerical measure of user satisfaction, it is based
  on three zones of application responsiveness:

  - Satisfied: The user is fully productive. This represents the
    time value (T seconds) below which users are not impeded by
    application response time.

  - Tolerating: The user notices performance lagging within
    responses greater than T, but continues the process.

  - Frustrated: Performance with a response time greater than 4*T
    seconds is unacceptable, and users may abandon the process.

    By default T is set to 1.5s this means that response time between 0
    and 1.5s the user is fully productive, between 1.5 and 6s the
    responsivness is tolerating and above 6s the user is frustrated.

    The Apdex score converts many measurements into one number on a
    uniform scale of 0-to-1 (0 = no users satisfied, 1 = all users
    satisfied).

    Visit http://www.apdex.org/ for more information.
* Rating: To ease interpretation the Apdex
  score is also represented as a rating:

  - U for UNACCEPTABLE represented in gray for a score between 0 and 0.5 

  - P for POOR represented in red for a score between 0.5 and 0.7

  - F for FAIR represented in yellow for a score between 0.7 and 0.85

  - G for Good represented in green for a score between 0.85 and 0.94

  - E for Excellent represented in blue for a score between 0.94 and 1.

Report generated with FunkLoad_ 1.16.1, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.