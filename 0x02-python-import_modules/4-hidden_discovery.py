#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    filenames = dir(hidden_4)
    for name in filenames:
        if name[:2] != "__":
            print("{}".format(name))
