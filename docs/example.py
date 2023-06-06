from virustotalpy import Scanner

API_KEY = "YOUR-API-KEY"
USER_NAME = "YOUR-VIRUSTOTAL-USERNAME"
scanner = Scanner(API_KEY, USER_NAME)

data = [
    "example.com",
    "192.168.0.1",
    "test.exe",
]

result = scanner.scan(data)
print(result)
