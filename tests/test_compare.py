#test_compare.py
#to run, execute this command line: 'python ./compare.py tornadoweb/tornado django/django pallets/flask'

import unittest
from mock import patch, Mock
import requests

import sys
from StringIO import StringIO
import os

import compare
from resources import constants
from tests.test_repo.test___init__ import fake_requests_get

if constants.UPDATE_JSON_FILES_CAPTURED:
    from tests.resources import json_file_downloader


class TestCompare(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        #update jsons files to run tests in a offline mode
        
        
        #to test 'compare'
        self.module_compare = compare
        self.arguments = constants.REPOS_URLS_PARTIAL_PATHS.values()
        
    def test_compare_compare(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            
            with patch('requests.get', side_effect = fake_requests_get) as mock_update_attrs:
                self.module_compare.compare(*self.arguments)
            if constants.DO_ONLINE_TESTS:
                self.module_compare.compare(*self.arguments)

            output = out.getvalue().strip()
            for line in output.splitlines():
                self.assertTrue(line[-1].isdigit())
                for piece in self.arguments + [': [', '] ']:
                    self.assertIn(piece, output)
        finally:
            sys.stdout = saved_stdout
            #print output
    
    def test_compare_main(self):
        pass
        #one not so useful unit test
        '''
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            #with patch('requests.get', side_effect = fake_requests_get) as mock_update_attrs:
            #    result = append(os.system('python compare.py ' + ' '.join(self.arguments)))
            #    self.assertEqual(result, 0) #not possible in Offline mode, probable because context 'with patch' does not affect 'os.system' command line
            if constants.DO_ONLINE_TESTS:
                result = os.system('python compare.py ' + ' '.join(self.arguments))
                self.assertEqual(result, 0) #only possible in Online mode, probable because context 'with patch' does not affect 'os.system' command line

            output = out.getvalue().strip()
            for line in output.splitlines():
                self.assertTrue(line[-1].isdigit())
                for piece in self.arguments + [': [', '] ']:
                    self.assertIn(piece, output)
        finally:
            sys.stdout = saved_stdout
            #print output
        '''

if __name__ == '__main__':
    unittest.main()
