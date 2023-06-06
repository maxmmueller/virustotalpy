# 2021-2023 Maximilian Müller - Apache License 2.0

import requests
import hashlib
import os
from base64 import urlsafe_b64encode
import re
import time
import sys

API_URL = "https://www.virustotal.com/api/v3/"


class vtError(Exception):
    def __init__(self, response):
        self.response = response

    # returns the error code and message returned from the API in a readable format
    def __str__(self):
        try:
            return f"Error {self.error().get('code')} {self.response.status_code}\n{self.error().get('message', '')}"
        except:
            return "Unknown Error"

    def error(self):
        return self.response.json().get("error")


class Scanner:
    def __init__(self, api_key, username):
        self.api_key = api_key
        self.profile_url = f"{API_URL}users/{username}"
        self.HEADERS = {"x-apikey": self.api_key}

    def is_quota_left(self):
        try:
            response = requests.get(self.profile_url, headers=self.HEADERS)
            response.raise_for_status()
            data = response.json()
            remaining_quota = data["data"]["attributes"]["quotas"]["api_requests_daily"]["allowed"]

        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")

        if remaining_quota > 0:
            return True
        return False

    def scan(self, resources: list) -> dict:
        """
        Scans resources for malicious properties

        :param resources: list of strings containing a file path, an url or an ip address
        :return: dictionary containing the scan results
        """

        resource_types = []

        # uploads every given resource to VirusTotal for a scan
        for resource in resources:
            if not self.is_quota_left():
                print("You have exceeded your API request rate and cousumed all your quota!")
                sys.exit()

            # checks if the given resource is a file path, an url or an ip address
            if os.path.isfile(resource):
                resource_type = "file"
            elif is_url(resource):
                resource_type = "url"
            elif is_ip_address(resource):
                resource_type = "ip_addresse"
            else:
                raise ValueError(f"Invalid resource type: {resource}")

            resource_types.append(resource_type)
            endpoint = f"{API_URL}{resource_type}s"

            if resource_type == "file":
                path_dict = {
                    "file": (
                        os.path.basename(resource),
                        open(os.path.abspath(resource), "rb"),
                    )
                }

                # files bigger than 32MB need a special url
                if os.path.getsize(resource) >= 32000000:
                    endpoint = large_file_url(self.api_key)

                try:
                    response = requests.post(
                        endpoint, files=path_dict, headers=self.HEADERS
                    )
                except:
                    raise MemoryError("Archive files are not allowed")

            elif resource_type == "url":
                response = requests.post(
                    endpoint, data={"url": resource}, headers=self.HEADERS
                )

        # gets the scan results for every given resource
        scan_results = {}
        for i, resource in enumerate(resources):
            #! walrus could be used
            response = get_scan_result(resource, resource_types[i], self.HEADERS)

            while len(response["last_analysis_results"]) <= 50:
                time.sleep(1)
                response = get_scan_result(resource, resource_types[i], self.HEADERS)

            scan_results[resources[i]] = response["last_analysis_stats"]

        return scan_results


def is_url(string):
    # regex pattern for URL validation
    pattern = re.compile(r"^(https?://)?([^\s/$.?#].[^\s]*)$")

    return re.match(pattern, string) is not None


def is_ip_address(string):
    pattern = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$"
    return re.match(pattern, string) is not None


def get_scan_result(resource, resource_type, headers):
    endpoint = f"{API_URL}{resource_type}s"

    if resource_type == "file":
        hash = sha1(resource)
        endpoint = f"{endpoint}/{hash}"

    elif resource_type == "url":
        url_id = urlsafe_b64encode(resource.encode()).decode().strip("=")
        endpoint = f"{endpoint}/{url_id}"

    elif resource_type == "ip_addresse":
        endpoint = f"{endpoint}/{resource}"

    response = requests.get(endpoint, headers=headers)
    data = dict(status_code=response.status_code, json_resp=response.json())

    if response.status_code != 200:
        raise vtError(response)
    else:
        return data["json_resp"]["data"]["attributes"]


# generates sha1 hash of the passed file
def sha1(filename):
    hash = hashlib.sha1()

    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            hash.update(chunk)

    return hash.hexdigest()


# files bigger than 32MB need a special url
def large_file_url(api_key):
    url = "https://www.virustotal.com/api/v3/files/upload_url"

    headers = {"Accept": "application/json", "x-apikey": api_key}

    response = requests.request("GET", url, headers=headers)
    return response.text[15:-3]
