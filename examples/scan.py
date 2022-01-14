from virustotalpy import Virustotal

# scan a file for malware
scanner = Virustotal('1dce0c1e8260ad7d7e95704c3be181a8c32060e9a6e170dba8547029d3c2fc00')
resp = scanner.api_request('post', path='C://Users//max20//Pictures//Hintergrund//rainbow mirror.jpeg')
resp = scanner.api_request('get', path='C://Users//max20//Pictures//Hintergrund//rainbow mirror.jpeg')
print(resp)

# scan a domain for malware
scanner = Virustotal("1dce0c1e8260ad7d7e95704c3be181a8c32060e9a6e170dba8547029d3c2fc00")
resp = scanner.api_request("post", url="https://en.wikipedia.org/wiki/Spider-Man_in_film")
resp = scanner.api_request("get", url="https://en.wikipedia.org/wiki/Spider-Man_in_film")
print(resp)
