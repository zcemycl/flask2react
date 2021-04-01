from app import *
import unittest
import json

def test_home():
    assert home.__name__=='home'

#class MyAppCase(unittest.TestCase):
#    def setUp(self):
#        app.config['TESTING'] = True
#        self.app = app.test_client()
#    def test_home(self):
#        resp = self.app.get('/')
#        data = json.loads(resp.get_data(as_text=True))
#        self.assertEqual(data['output'],'Hello World')
