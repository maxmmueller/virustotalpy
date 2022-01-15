# virustotalpy
Virustotalpy is library for an easier interaction with the [VirusTotal](https://www.virustotal.com/) v3 api

## Installation ⚙️
> Requires Python 3.7 or newer.
```
pip install virustotalpy
```

## Usage 🚀
>In order to get a VirusTotal api-key, you need to [sign up](https://www.virustotal.com/gui/join-us) for an account
>
> ![VirusTotal view API key](imgs/APIKey.jpeg)


- Upload a file to be analyzed and scanned for malware:
```python
from virustotalpy import Virustotal

# first initialise the Virustotal class
scanner = Virustotal('YOUR_API_KEY')

# make api request
resp = scanner.api_request('post', path='PATH_TO_FILE')
```
- Obtain information about the file:
> NOTE: To get this information, you must use the "post" method first.

```python
resp = scanner.api_request('get', path='PATH_TO_FILE')
print(resp)
```

- more [examples](examples)

## Learn more 🔗:

- [Docs](https://pypi.org/project/virustotalpy/)
- [API](https://developers.virustotal.com/reference/overview)


## License 📃

Copyright © 2021-2022 Maximilian Müller.
[Apache License 2.0](LICENSE).