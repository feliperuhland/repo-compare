#run this command to test all: python -m unittest discover -s tests -v

import unittest
from mock import patch, Mock
import requests
from urlparse import urlparse

import copy
import os.path
import sys
from StringIO import StringIO

import repo
from resources import constants

#Return a fake response from a loaded json filesystem by url_path
def fake_requests_get(url):
    parsed_url = urlparse(url)
    repo_full_name_from_url = parsed_url.path.split('/',2)[2]
    repo_full_name = repo_full_name_from_url.replace('/','_')
    resource_file = os.path.normpath(
        constants.RESPONSES_IN_JSON_FILES_DIR_PATH
        + repo_full_name
        + '.json')
    faked_response = requests.models.Response()
    faked_response.status_code = 200
    faked_response.headers = constants.FAKE_RESPONSE_HEADERS
    with open(resource_file, mode='rb') as f:
        data = f.read()
        faked_response._content = data
    return faked_response


class TestRepo(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        #to test 'repo' module (before its __init__)
        #to test 'variable_GITHUB_URL'
        #to test 'get_bar'
        #to test 'Report_show_result'
        self.module_repo = repo
        
        #to test 'Repo.__init__'
        #to test 'Repo.__repr__'
        with patch('repo.Repo._update_attrs') as mock_update_attrs:
            mock_update_attrs.return_value = 'faked_function'
            self.fullnamerepo = repo.Repo('My Full Name Repo')
            self.nonenamerepo = repo.Repo(None) #'My None Name Repo'
            self.emptynamerepo = repo.Repo('') #'My Empty Name Repo'
        
        #to test 'Repo__update_attrs'
        self.repos_initiated = {}
        self.repos_to_check_online = {}
        self.repos_to_check_offline = {}
        with patch('repo.Repo._update_attrs') as mock_update_attrs:
            mock_update_attrs.return_value = 'faked_function'
            for k,v in constants.REPOS_URLS_PARTIAL_PATHS.iteritems():
                self.repos_initiated[k] = repo.Repo(full_name = v)
        self.repos_to_check_offline = copy.deepcopy(self.repos_initiated)
        if constants.DO_ONLINE_TESTS:
            self.repos_to_check_online = copy.deepcopy(self.repos_initiated)
            for dict_repos in [self.repos_to_check_online, self.repos_to_check_offline]:
                for k,rep in dict_repos.iteritems():
                    repo.Repo._update_attrs(rep, rep.full_name)
        with patch('requests.get', side_effect = fake_requests_get) as mock_update_attrs:
            for k,rep in self.repos_to_check_offline.iteritems():
                repo.Repo._update_attrs(rep, rep.full_name)
        
        #to test 'Report_fields'
        ##nothing needed to be initiated
        
        #to test 'Report.__init__'
        #to test 'Report.get_best_value'
        #to test 'Report.test_score'
        #to test 'Report_show_result'
        self.report_offline = repo.Report(self.repos_to_check_offline.values())
        self.report_repos = [(self.report_offline, self.repos_to_check_offline.values())]
        if constants.DO_ONLINE_TESTS:
            self.report_online = repo.Report(self.repos_to_check_online.values())
            self.report_repos.append((self.report_online, self.repos_to_check_online.values()))
        
        
    
    def test_variable_GITHUB_URL(self):
        self.assertEqual(self.module_repo.GITHUB_URL, constants.GITHUB_API_URL)
    
    def test_get_bar(self):
        self.assertEqual(self.module_repo._get_bar(0,0), '')
        
        self.assertEqual(self.module_repo._get_bar(1,6), '+     ')
        self.assertEqual(self.module_repo._get_bar(2,6), '++    ')
        self.assertEqual(self.module_repo._get_bar(3,6), '+++   ')
        self.assertEqual(self.module_repo._get_bar(4,6), '++++  ')
        self.assertEqual(self.module_repo._get_bar(5,6), '+++++ ')
        self.assertEqual(self.module_repo._get_bar(6,6), '++++++')
        
        self.assertEqual(self.module_repo._get_bar(6,1), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,2), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,3), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,4), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,5), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,6), '++++++')
                
        self.assertEqual(self.module_repo._get_bar(-1,6), '       ')
        self.assertEqual(self.module_repo._get_bar(-2,6), '        ')
        self.assertEqual(self.module_repo._get_bar(-3,6), '         ')
        self.assertEqual(self.module_repo._get_bar(-4,6), '          ')
        self.assertEqual(self.module_repo._get_bar(-5,6), '           ')
        self.assertEqual(self.module_repo._get_bar(-6,6), '            ')
        
        self.assertEqual(self.module_repo._get_bar(-6,1), '       ')
        self.assertEqual(self.module_repo._get_bar(-6,2), '        ')
        self.assertEqual(self.module_repo._get_bar(-6,3), '         ')
        self.assertEqual(self.module_repo._get_bar(-6,4), '          ')
        self.assertEqual(self.module_repo._get_bar(-6,5), '           ')
        self.assertEqual(self.module_repo._get_bar(-6,6), '            ')
        
        self.assertEqual(self.module_repo._get_bar(1,-6), '+')
        self.assertEqual(self.module_repo._get_bar(2,-6), '++')
        self.assertEqual(self.module_repo._get_bar(3,-6), '+++')
        self.assertEqual(self.module_repo._get_bar(4,-6), '++++')
        self.assertEqual(self.module_repo._get_bar(5,-6), '+++++')
        self.assertEqual(self.module_repo._get_bar(6,-6), '++++++')
        
        self.assertEqual(self.module_repo._get_bar(6,-1), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,-2), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,-3), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,-4), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,-5), '++++++')
        self.assertEqual(self.module_repo._get_bar(6,-6), '++++++')

        self.assertEqual(self.module_repo._get_bar(-1,-6), '')
        self.assertEqual(self.module_repo._get_bar(-2,-6), '')
        self.assertEqual(self.module_repo._get_bar(-3,-6), '')
        self.assertEqual(self.module_repo._get_bar(-4,-6), '')
        self.assertEqual(self.module_repo._get_bar(-5,-6), '')
        self.assertEqual(self.module_repo._get_bar(-6,-6), '')

        self.assertEqual(self.module_repo._get_bar(-6,-1), '     ')
        self.assertEqual(self.module_repo._get_bar(-6,-2), '    ')
        self.assertEqual(self.module_repo._get_bar(-6,-3), '   ')
        self.assertEqual(self.module_repo._get_bar(-6,-4), '  ')
        self.assertEqual(self.module_repo._get_bar(-6,-5), ' ')
        self.assertEqual(self.module_repo._get_bar(-6,-6), '')

    @patch('repo.Repo._update_attrs')
    def test_Repo___init__(self, mock_update_attrs):
        mock_update_attrs.return_value = 'faked_function'
        
        self.assertEqual(self.fullnamerepo.full_name, 'My Full Name Repo')
        self.assertEqual(self.nonenamerepo.full_name, None)
        self.assertEqual(self.emptynamerepo.full_name, '')
        
        for r in [self.fullnamerepo, self.nonenamerepo, self.emptynamerepo]:
            self.assertEqual(r.name, None)
            self.assertEqual(r.stars, None)
            self.assertEqual(r.forks, None)
            self.assertEqual(r.subscribers, None)
            self.assertEqual(r.pushed_at, None)
            self.assertEqual(r.created_at, None)
            self.assertEqual(r.updated_at, None)
            self.assertEqual(r._update_attrs(r.full_name), 'faked_function')

    def test_Repo__update_attrs(self):
        for dict_repos in [self.repos_to_check_offline, self.repos_to_check_online]:
            for key, rep in dict_repos.iteritems():
                self.assertEqual(rep.full_name, constants.REPOS_URLS_PARTIAL_PATHS[key])
                self.assertIsInstance(rep.full_name, str)
                self.assertIsInstance(rep.name, unicode)
                self.assertIsInstance(rep.stars, int)
                self.assertIsInstance(rep.forks, int)
                self.assertIsInstance(rep.subscribers, int)
                self.assertIsInstance(rep.pushed_at, unicode)
                self.assertIsInstance(rep.created_at, unicode)
                self.assertIsInstance(rep.updated_at, unicode)
    
    @patch('repo.Repo._update_attrs')
    def test_Repo___repr__(self, mock_update_attrs):
        mock_update_attrs.return_value = 'faked_function'
        
        self.assertEqual(self.fullnamerepo.full_name, 'My Full Name Repo')
        self.assertEqual(self.nonenamerepo.full_name, None)
        self.assertEqual(self.emptynamerepo.full_name, '')
        
        self.assertEqual(self.fullnamerepo.__repr__(), '<Repo: My Full Name Repo>')
        self.assertEqual(self.nonenamerepo.__repr__(), '<Repo: None>')
        self.assertEqual(self.emptynamerepo.__repr__(), '<Repo: >')
        
        self.assertEqual(repr(self.fullnamerepo), '<Repo: My Full Name Repo>')
        self.assertEqual(repr(self.nonenamerepo), '<Repo: None>')
        self.assertEqual(repr(self.emptynamerepo), '<Repo: >')
    
    def test_Report_fields(self):
        self.assertEqual(repo.Report.fields, constants.FAKE_FIELDS)
        for k,v in constants.FAKE_FIELDS.iteritems():
            self.assertEqual(repo.Report.fields[k] , v)
    
    def test_Report___init__(self):
        for report, repos in self.report_repos:
            self.assertIsInstance(report, repo.Report)
            self.assertEqual(report.repos, repos)
            self.assertEqual(report.score, {r.full_name: {'total': 0} for r in repos})
            self.assertEqual(report.col_width, max(len(r.full_name) for r in repos))
    
    def test_Report_get_best_value(self):
        for report, repos in self.report_repos:
            values_per_field = {}
            for field in report.fields:
                values_per_field[str(field)] = [getattr(repo,str(field)) for repo in report.repos]
                for function in [min, max]:
                    self.assertEqual(function(values_per_field[field]), report.get_best_value(function, field))
    
    def test_Report_test_score(self):
        for report, repos in copy.deepcopy(self.report_repos):
            self.assertEqual(report.score, {r.full_name: {'total': 0} for r in repos})
            report.test_score()
            self.assertNotEqual(report.score, {r.full_name: {'total': 0} for r in repos})
            self.assertEqual(len(report.score), len(report.repos))
            self.assertEqual(len(report.score), len(repos))
            for dict_scores in report.score.values():
                score_pieces_summed = sum(v for k,v in dict_scores.iteritems() if k != 'total')
                score_total = dict_scores['total']
                self.assertEqual(score_pieces_summed, score_total)
    
    def test_Report_show_result(self):
        for report, repos in copy.deepcopy(self.report_repos):
            self.assertEqual(report.score, {r.full_name: {'total': 0} for r in repos})
            report.test_score()
            self.assertNotEqual(report.score, {r.full_name: {'total': 0} for r in repos})
            
            saved_stdout = sys.stdout
            try:
                out = StringIO()
                sys.stdout = out
                report.show_result()
                output = out.getvalue().strip()
                for repo in report.repos:
                    sub_result_string = (
                        repo.full_name.ljust(report.col_width) 
                        + ': ['
                        + self.module_repo._get_bar(report.score[repo.full_name]['total'], len(report.fields))
                        + '] '
                        + str(report.score[repo.full_name]['total'])
                    )
                    self.assertIn(sub_result_string, output)
                self.assertEqual(report.col_width, max(len(repo.full_name) for repo in report.repos))
            finally:
                sys.stdout = saved_stdout
                #print output

if __name__ == '__main__':
    unittest.main()
