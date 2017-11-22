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

    @data(*getCsvData('reverse.csv'))
    @unpack
    def testAddress(self,  val1, val2, address):
        """test case for scenario a"""
        driver = self.driver
        url = "http://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" + val1 + "&lon=" + val2
        response = requests.get(url)
        driver.implicitly_wait(2)
        resp = response.json()
        jstr = resp['display_name']
        self.assertTrue(address in jstr.strip())


    @classmethod
    def tearDownClass(cls):
        """clean up"""
        cls.driver.close()

