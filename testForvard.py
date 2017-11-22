import unittest

import requests

from ddt import ddt, data, unpack
from selenium import webdriver



def getCsvData(csvPath):
    rows = []
    csvData = open(csvPath)

    for row in csvData:
        list = row.strip().split(";")
        rows.append(list)
    return rows

@ddt
class TestAddress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """test preparation"""
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(2)

    @data(*getCsvData('forvard.csv'))
    @unpack
    def testAddress(self, address, val1, val2):
        """test case for scenario a"""
        driver = self.driver
        url = "http://nominatim.openstreetmap.org/search/" + address + "?format=json&addressdetails=1&limit=1&polygon_svg=1"
        response = requests.get(url)
        driver.implicitly_wait(2)
        resp = response.json()
        jstr1 = resp[0]['lat']
        jstr2 = resp[0]['lon']
        #print(jstr1 + " " + jstr2 + " "+ address) #для проверки значений вывода json

        self.assertTrue(val1 in str(jstr1))
        self.assertTrue(val2 in str(jstr2))

    @classmethod
    def tearDownClass(cls):
        """clean up"""
        cls.driver.close()

