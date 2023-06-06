<h1 align="center">
<sub>
<img src="imgs/vt_logo.jpeg" height="30">
</sub>
VirusTotalPy
</h1>

<p align="center">
<img src="https://img.shields.io/pypi/v/virustotalpy.svg?style=square">
<img src="https://img.shields.io/badge/license-Apache%202-blue">
<a href="https://github.com/maxmmueller/virustotalpy/blob/main/LICENSE"></a>
</p>

<p align="center">Open-source Python library for an easier interaction with the VirusTotal v3 API</p>


## Features
The latest Version 1.0 lets you analyse and scan a list of IPs, URLs and files up to 650MB.

## Installation
##### Method 1:
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Requires-Python%203.6%20(or%20newer)-blue"/></a>
```
pip install virustotalpy
```

##### Method 2:
 <a href="https://git-scm.com/downloads"><img src="https://img.shields.io/badge/Requires-git-blue"/></a>

```
git clone https://github.com/maxmmueller/virustotalpy.git
```

##### Method 3:
Download the [latest Release](https://github.com/maxmmueller/virustotalpy/releases/latest)


## Usage
In order to use the API you need to [sign up](https://www.virustotal.com/gui/join-us) for a VirusTotal account and create an API key.
>
> ![View API key](imgs/api_key.jpeg)

Code example:
```python
from virustotalpy import Scanner

# replace this with your actual api key and username
API_KEY = "YOUR-API-KEY"
USER_NAME = "YOUR-VIRUSTOTAL-USERNAME"

scanner = Scanner(API_KEY, USER_NAME)

data = [
    "https://www.example.com",
    "192.168.0.1",
    "test.exe"
]

result = scanner.scan(data)
print(result)
```

## Learn more

- [Documentation and reference](docs/docs.md)
- [PyPI](https://pypi.org/project/virustotalpy)
- [API reference](https://developers.virustotal.com/reference/overview)

## Contributing
Contributions to this project are welcome!

If you encounter any problems, find a bug or have feature requests, please open an [issue](https://github.com/maxmmueller/virustotalpy/issues/new).

## Licence
Maximilian Müller 2021-2023
[Apache License 2.0](LICENSE)