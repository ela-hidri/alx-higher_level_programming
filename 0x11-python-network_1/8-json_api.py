#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv[1]) == 1:
        q = argv[1]
    else:
        q = ""
    values = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=values)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
