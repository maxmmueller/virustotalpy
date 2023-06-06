# Use the VirusTotalPy library 
## `scan(resources: list) -> dict`

Scans resources for malicious properties.

- Parameters:
  - `resources` (list): A list of strings containing file paths, URLs, or IP addresses to be scanned.

- Returns:
  - A dictionary containing the scan results. The keys of the dictionary are the resources, and the values are the scan results.

### Example

Replace this with your actual api key and username
```python
API_KEY = "YOUR-API-KEY"
USER_NAME = "YOUR-VIRUSTOTAL-USERNAME"

scanner = Scanner(API_KEY, USER_NAME)
```
Create a list containing the resources you want to scan and provide it as the parameter for the `scan` function
```python
resources = ['example.com', '192.168.0.1', 'test.exe']
scan_results = scanner.scan(resources)
```
The scan_results dictionary will contain the results for each resource:

```python
{
    'example.com': {
        'harmless': 73, 
        'malicious': 0, 
        'suspicious': 0, 
        ...
    }, 
        
    '192.168.0.1': {
        'harmless': 71, 
        'malicious': 0, 
        'suspicious': 0,
        ...
    }, 
    
    'test.exe': {
        'harmless': 0, 
        'suspicious': 0,
        'malicious': 0, 
        'undetected': 59,
        ...
    }
}
```
[more examples](example.py)

Note: The exact attributes and their meanings can be found in the VirusTotal API documentation.