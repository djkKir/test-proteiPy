import unittest
import requests
from ddt import ddt, data, unpack
from readFile import getCsvData

#проверка координат по введенному адресу
@ddt
class TestPosition(unittest.TestCase):

    @data(*getCsvData('forvard.csv'))
    @unpack
    def testPosition(self, address, lat0, lon0, lat1, lon1):
        #  посылаем запрос, ожидаем json ответ
        url = "http://nominatim.openstreetmap.org/search/"+\
              address +\
              "?format=json&addressdetails=1&limit=1&polygon_svg=1"
        response = requests.get(url)
        resp = response.json()
        # получаем координаты
        lat = resp[0]['lat']
        lon = resp[0]['lon']
        # сравниваем полученный результат с тестовой областью
        islat = (lat > lat0) & (lat < lat1)
        islon = (lon > lon0) & (lon < lon1)

        self.assertTrue(islat & islon)







