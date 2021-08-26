from scrapy.http import HtmlResponse
import grp12
import requests
import unittest
from unittest import TestCase
import json

session = requests.Session()

class test_part5(TestCase):
    def test_sc(self):
        response = requests.get(grp12.url)
        self.assertEqual(response.status_code, 200)

    def mua(self):
        responseua = grp12.modified_ua
        self.assertEqual(responseua.request.headers, {'User-Agent': 'Mobile', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'})


class test_file(TestCase):
    def test_json(self):
        f = open("resultss.json",)
        data_jpg = json.loads(f.read())
        self.assertEqual(data_jpg[1], {'Image Link': 'https://images.brickset.com/sets/small/3594-1.jpg?200811140307'})

        f.close()


if __name__ == '__main__':
    unittest.main()

