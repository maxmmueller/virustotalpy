# (c) 2021-2022 Maximilian Müller - Apache License 2.0

# virustotalpy is a library for an easier interaction with the v3 api
# powered by https://www.virustotal.com

import requests
import hashlib
import os
from base64 import urlsafe_b64encode


# class for VirusTotal API errors
class vtError(Exception):

    def __init__(self, response):
        self.resp = response

    # returns the error code and message returned from the API in a readable format
    def __str__(self):
        try:
            return f"Error {self.error().get('code')} {self.resp.status_code}\n{self.error().get('message', '')}"
        except:
            return "Unknown Error"


    def error(self):
        return self.resp.json().get("error")


class Virustotal:
    def __init__(self, api_key):
        self.api_key = api_key

    def api_request(self, method, path=None, url=None):
        """
        Sends a request to the VirusTotal API
        :param method: specifies the request method to be used
        :param path: valid path for the file to be used within the request
        :param url: valid url for the domain to be used within the request
        :returns: dictionary with the request-response
        """

        BASE_URL = "https://www.virustotal.com/api/v3/"
        HEADERS = {
            "x-apikey": f"{self.api_key}"
        }

        # checks if the given resource is a file or a url
        if url == None and path != None:
            resource = "file"
            endpoint = BASE_URL + "files"
        elif path == None and url != None:
            resource = "url"
            endpoint = BASE_URL + "urls"
        else:
            raise ValueError("No file path or url was given")

        if method == "post":
            if resource == "file":
                path = {"file": (os.path.basename(path), open(os.path.abspath(path), "rb"))}
                response = requests.post(endpoint, files=path, headers=HEADERS)

            elif resource == "url":
                response = requests.post(endpoint, data={"url": url}, headers=HEADERS)

            data = dict(status_code=response.status_code, json_resp=response.json())
            return data

        elif method == "get":
            if resource == "file":
                endpoint = f"{endpoint}/{sha1(path)}"

            elif resource == "url":
                url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
                endpoint = f"{endpoint}/{url_id}"

            response = requests.get(endpoint, headers=HEADERS)
            data = dict(status_code=response.status_code, json_resp=response.json())

            if response.status_code != 200:
                raise vtError(response)
            else:
                return data['json_resp']["data"]["attributes"]


# generates sha1 hash of the passed file
def sha1(filename):
    hash = hashlib.sha1()

    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            hash.update(chunk)

    return hash.hexdigest()