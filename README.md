# virustotalpy
Virustotalpy is python library for an easier interaction with the public VirusTotal [v3 api](https://developers.virustotal.com/reference/overview). Virustotalpy v0.2.x let's you analyse and scan IPs, URLs and files up to 650MB.

## Installation
##### Method 1:
> Requires [Python](https://www.python.org/downloads/) 3.6 or newer.
```
pip install virustotalpy
```

##### Method 2:
> Requires [git](https://git-scm.com/downloads) 
```
git clone https://github.com/maxmmueller/virustotalpy.git
```

##### Method 3:
Download the [latest Release](https://github.com/maxmmueller/virustotalpy/releases/latest)


## Usage
>In order to get a VirusTotal api-key, you need to [sign up](https://www.virustotal.com/gui/join-us) for an account
>
> ![VirusTotal view API key](https://raw.githubusercontent.com/maxmmueller/virustotalpy/master/imgs/APIKey.jpeg)


At first the Virustotal class has to be initialised
```python
from virustotalpy import Virustotal

scanner = Virustotal('YOUR_API_KEY')
```
#### Files
- make api request
```python
resp = scanner.api_request('post', path='PATH_TO_FILE')
```
- Obtain information about the file:
> NOTE: To get this information, you have to use the "post" method first.

```python
resp = scanner.api_request('get', path='PATH_TO_FILE')
print(resp)
```

#### URLs

- make api request
```
resp = scanner.api_request('post', path='URL')
```
- Obtain information about the url:
> NOTE: To get this information, you have to use the "post" method first.

```python
resp = scanner.api_request('get', path='URL')
print(resp)
```

- more [examples](examples)

## Learn more

- [PyPI](https://pypi.org/project/virustotalpy)
- [API](https://developers.virustotal.com/reference/overview)

## License

Copyright © 2021-2022 Maximilian Müller.
[Apache License 2.0](LICENSE).