#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    values = {"email": str(argv[2])}
    url = argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        resp = res.read()
        print(resp.decode('utf-8'))
