#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv
    try:
        with urllib.request.urlopen(argv[1]) as res:
            resp = res.read()
            print(resp.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
