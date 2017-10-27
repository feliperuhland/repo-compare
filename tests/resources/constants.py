#constants.py
#All the SAME constants to be used by many tests

#UPDATE_JSON_FILES_CAPTURED
#boolean (default: 'False')
#Mark 'False' to not update your jsons files, from Github API by running 'json_file_downloader.py'.
#Mark 'True' to update your jsons files, from Github API by running 'json_file_downloader.py'.
#The 'json_file_downloader.py' gets newest jsons to be used in offline tests and, stores all old jsons in a proper datetimed subfolder.
UPDATE_JSON_FILES_CAPTURED = False

#DO_ONLINE_TESTS
#boolean (default: 'False')
#Mark 'False' to run only offline tests, and 'True' to run online tests. 
#If you mark 'True', the online tests will consume two things from you:
#1- Your internet bandwith;
#2- Your accesses in Github API (https://developer.github.com/v3/rate_limit/).
DO_ONLINE_TESTS = False

#RESPONSES_IN_JSON_FILES_DIR_PATH
#string (default: './tests/resources/json_files_captured/latest_json_files_captured/')
#Points to directory (folder) that contains all *.json responses exported from Github API.
#The json are used in offline tests, helping in simulate the responses.
#The folder contains only json from 3 repositories used in tests (django, tornado, flask).
RESPONSES_IN_JSON_FILES_DIR_PATH = './tests/resources/json_files_captured/latest_json_files_captured/'

#FAKE_RESPONSE_HEADERS
#dict (default: cames from one online 'request.get', like below)
#>>> import requests
#>>> response = requests.get('https://api.github.com/repos/pallets/flask')
#>>> response.headers
FAKE_RESPONSE_HEADERS = {
    'Expect-CT': 'max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"', 
    'X-XSS-Protection': '1; mode=block', 
    'Content-Security-Policy': "default-src 'none'", 
    'Access-Control-Expose-Headers': 'ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval', 
    'Transfer-Encoding': 'chunked', 
    'Last-Modified': 'Sun, 22 Oct 2017 15:24:11 GMT', 
    'Access-Control-Allow-Origin': '*', 
    'X-Frame-Options': 'deny', 
    'Status': '200 OK', 
    'X-GitHub-Request-Id': '69D5:27DA5:9F027D:164F214:59ECBF56', 
    'ETag': 'W/"9be12b1365819c8d7c1a0b86e1a16b44"', 
    'Date': 'Sun, 22 Oct 2017 15:55:02 GMT', 
    'X-RateLimit-Remaining': '28', 
    'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 
    'Server': 'GitHub.com', 
    'X-GitHub-Media-Type': 'github.v3; format=json', 
    'X-Content-Type-Options': 'nosniff', 
    'Content-Encoding': 'gzip', 
    'X-Runtime-rack': '0.038494', 
    'Vary': 'Accept', 
    'X-RateLimit-Limit': '60', 
    'Cache-Control': 'public, max-age=60, s-maxage=60', 
    'Content-Type': 'application/json; charset=utf-8', 
    'X-RateLimit-Reset': '1508688222'
}

#GITHUB_API_URL
#string (default: 'https://api.github.com/repos')
#Contains the first part of the Github url path
GITHUB_API_URL = 'https://api.github.com/repos'

#REPOS_URLS_PARTIAL_PATHS
#dict (default: {'repo_flask': 'pallets/flask', 'repo_django': 'django/django', 'repo_tornado': 'tornadoweb/tornado'})
#Distribute all partial url paths from the tested repositories (Flask, Django, Tornado).
# These partial urls will compound the full urls, to be:
#1- Flask: https://api.github.com/repos/pallets/flask
#2- Django: https://api.github.com/repos/django/django
#3- Tornado: https://api.github.com/repos/tornadoweb/tornado
REPOS_URLS_PARTIAL_PATHS = {
    'repo_flask'   : 'pallets/flask', 
    'repo_django'  : 'django/django', 
    'repo_tornado' : 'tornadoweb/tornado'
}

#FAKE_FIELDS
#dict (default: {'created_at': min, 'forks': max, 'pushed_at': max, 'stars': max, 'subscribers': max, 'updated_at': max,})
#Replicate the comparable repositories fields and their functions to be evaluated.
FAKE_FIELDS = {
    'created_at': min,
    'forks': max,
    'pushed_at': max,
    'stars': max,
    'subscribers': max,
    'updated_at': max,
}
