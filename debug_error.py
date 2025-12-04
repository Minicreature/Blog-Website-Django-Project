import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://127.0.0.1:8001/')
    with open('error_full.html', 'w', encoding='utf-8') as f:
        f.write(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    with open('error_full.html', 'w', encoding='utf-8') as f:
        f.write(e.read().decode('utf-8'))
except Exception as e:
    print(e)
