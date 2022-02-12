from virustotalpy import Virustotal

# scan a file for malware
scanner = Virustotal("API_KEY")
resp = scanner.api_request('post', path='PATH')
resp = scanner.api_request('get', path='PATH')
print(resp)

# scan a domain for malware
scanner = Virustotal("API_KEY")
resp = scanner.api_request("post", url="URL")
resp = scanner.api_request("get", url="URL")
print(resp)
