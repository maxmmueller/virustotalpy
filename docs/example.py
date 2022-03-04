from virustotalpy import Virustotal

vt = Virustotal("API_KEY")

# scan a file for malware
vt.api_request("post", path="PATH")
resp = vt.api_request("get", path="PATH")
print(resp)

# scan a domain for malware
vt.api_request("post", url="URL")
resp = vt.api_request("get", url="URL")
print(resp)

# scan an ip-adress for malware
resp = vt.api_request("get", ip="IP")
print(resp)