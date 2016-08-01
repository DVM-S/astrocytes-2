import requests
import inspect

from collections import OrderedDict
from requests.auth import HTTPBasicAuth

HOST = 'http://astrocytes.azurewebsites.net/'
API_ENDPOINT = 'api/v1/'
API_URL = HOST + API_ENDPOINT
JSON_HEADER = {'Content-type': 'application/json'}
GAMES = (
    ('punch', 'Punch Me'),
    ('rain', 'Falling Knowledge'),
    ('time', 'Tell The Time'),
    ('walking', 'This or That'),
)

# ------------------------------------------------------------------------
# Helper Functions


def extend_headers_with_auth(func):
    def _func(*orignal_args):
        args, varargs, keywords, defaults = inspect.getargspec(func)
        args_passed = OrderedDict(zip(args, orignal_args))
        default_args = OrderedDict(zip(args[-len(defaults):], defaults))
        args_passed.update(default_args)
        auth_headers = {'Authorization': 'ApiKey %s:%s' %
                        (args_passed['username'], args_passed['api_key'])}
        args_passed['headers'].update(auth_headers)
        args = args_passed.values()
        return func(*args)
    return _func


def make_handle_request(resource, headers, r_type, data=None, params={"game": None}):

    url = API_URL + resource
    if r_type == 'GET':
        try:
            r = requests.get(url, headers=headers, params=params)
        except requests.exceptions.Timeout:
            "Checking your Internet Connection."
            if check_internet():
                try:
                    r = requests.get(url, headers=headers, params=params)
                except requests.exceptions.Timeout:
                    print 'The servers are currently down'
                    return None
            else:
                print "Please connect to the internet."
                return None
        except requests.exceptions.RequestException as e:
            print "An Unknow error occured"
            return None

    elif r_type == 'POST':
        try:
            r = requests.post(url, data=data, headers=headers)
        except requests.exceptions.Timeout:
            "Checking your Internet Connection."
            if check_internet():
                try:
                    r = requests.post(url, data=data, headers=headers)
                except requests.exceptions.Timeout:
                    print 'The servers are currently down'
                    return None
            else:
                print "Please connect to the internet."
                return None
        except requests.exceptions.RequestException as e:
            print "Fatal error %s" % e
            return None

    if r.status_code == 401:
        print "Acess Denied"
        return None

    elif r.status_code == 200:
        return r.json()

    elif r.status_code == 201:
        return True

    else:
        print r.status_code, "status code"


def check_internet():
    try:
        requests.get('http://www.microsoft.com')
        return True
    except:
        return False


# ------------------------------------------------------------------------
# API

@extend_headers_with_auth
def get_profile(username, api_key, headers={}, resource='profile/'):
    response = make_handle_request(resource, headers, 'GET')
    if response is not None:
        return response


def get_api_key(username, password, resource='user/'):
    url = API_URL + resource
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    if r.status_code == 200:
        response = r.json()
        return str(response['api-key'])
    raise Exception("Authentication Failed")


@extend_headers_with_auth
def get_user_level(username, api_key, game,
                   headers={}, resource='userlevel/'):

    params = {"game": game}
    response = make_handle_request(resource, headers, 'GET', params=params)
    if response is not None and len(response['objects']):
        return response['objects'][0]['level']


@extend_headers_with_auth
def save_game_record(username, api_key, game, score,
                     headers=JSON_HEADER, resource='records/'):
    data = {
        "game": game,
        "score": score,
    }
    return make_handle_request(resource, headers, 'POST', data=data)


@extend_headers_with_auth
def get_game_records(username, api_key, game, headers={},
                     resource='records/'):
    params = {"game": game}
    response = make_handle_request(resource, headers, 'GET', params=params)
    if response is not None:
        return response['objects']


@extend_headers_with_auth
def get_questions(username, api_key, game, level,
                  headers={}, resource='question/'):
    params = {"game": game, "level": level}
    response = make_handle_request(resource, headers, 'GET', params=params)
    if response is not None:
        return response['objects']
