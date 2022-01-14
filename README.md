# virustotalpy
Virustotalpy is library for an easier interaction with the [VirusTotal](https://www.virustotal.com/) v3 api

## Installation ⚙️
> NOTE
> Requires Python 3.7 or newer.
```
pip install virustotalpy
```

## Usage 🚀
>In order to get a [VirusTotal](https://www.virustotal.com/) api-key you need to create an account
> ![VirusTotal view API key](imgs/APIKey.jpeg)
- Scan a file for malware:
```python
from virustotalpy import Virustotal

scanner = Virustotal('YOUR_API_KEY')

# upload the file to be scanned
resp = scanner.api_request('post', path='PATH_TO_FILE')
# get the result
resp = scanner.api_request('get', path='PATH_TO_FILE')
```