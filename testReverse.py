import unittest
import requests

from readFile import getCsvData
from ddt import ddt, data, unpack

# тест адреса по введенным координатам
@ddt
class TestAddress(unittest.TestCase):

    @data(*getCsvData('reverse2.csv'))
    @unpack
    def testAddress(self,  lat0, lon0, address):
        # посылаем запрос, ожидаем json ответ
        url = "http://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" + lat0 + "&lon=" + lon0
        response = requests.get(url)
        resp = response.json()
        # из ответа получаем адрес (избыточный, надо подкорректировать)
        adr = resp['display_name']
        # сравниваем полученную строку с тестовой
        self.assertTrue(address in adr.strip())




