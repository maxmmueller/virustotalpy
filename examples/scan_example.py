from virustotalpy import Virustotal

# scan a file for malware
scanner = Virustotal("API_KEY")
resp = scanner.api_request('post', path='C://Users//max20//Pictures//Hintergrund//rainbow mirror.jpeg')
resp = scanner.api_request('get', path='C://Users//max20//Pictures//Hintergrund//rainbow mirror.jpeg')
print(resp)

# scan a domain for malware
scanner = Virustotal("API_KEY")
resp = scanner.api_request("post", url="https://en.wikipedia.org/wiki/Spider-Man_in_film")
resp = scanner.api_request("get", url="https://en.wikipedia.org/wiki/Spider-Man_in_film")
print(resp)
