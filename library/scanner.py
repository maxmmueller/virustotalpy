import requests
import hashlib
import os

# generates sha1 hash of the passed file
def sha1(filename):
    hash = hashlib.sha1()

    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            hash.update(chunk)

    return hash.hexdigest()


def api_request(method, api_key, path=None, url=None):

    BASE_URL = 'https://www.virustotal.com//api/v3/'
    HEADERS = {
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': f'gzip, virustotal-python 0.1.3',
        'x-apikey': f'{api_key}'
    }

    # checks if the given resource is a file or a url
    if url == None and path != None:
        endpoint = BASE_URL + 'files'
    elif path == None and url != None:
        endpoint = BASE_URL + 'url'
    else:
        raise ValueError('No file path or url was given')

    if method == 'post':
        path = {'file': (os.path.basename(path), open(os.path.abspath(path), 'rb'))}
        response = requests.post(endpoint, files=path, headers=HEADERS)
        # response = response.json()
        data = dict(status_code=response.status_code, json_resp=response.json())
        return data

    elif method == 'get':
        if path != None:
            endpoint = f'{endpoint}/{sha1(path)}'
        else:
            endpoint = f'{endpoint}/{url}'

        response = requests.get(endpoint, headers=HEADERS)
        data = dict(status_code=response.status_code, json_resp=response.json())
        return data
