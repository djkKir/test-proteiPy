import unittest

import requests

from readFile import getCsvData
from ddt import ddt, data, unpack


@ddt
class TestAddress(unittest.TestCase):


    @data(*getCsvData('reverse2.csv'))
    @unpack
    def testAddress(self,  lat0, lon0, address):

        url = "http://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" + lat0 + "&lon=" + lon0
        response = requests.get(url)

        resp = response.json()
        adr = resp['display_name']
        print("---------------")
        print(address)
        print(adr)
        self.assertTrue(address in adr.strip())




