#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    values = {"email": str(argv[2])}
    r = requests.post(argv[1], data=values).text
    print(r)
