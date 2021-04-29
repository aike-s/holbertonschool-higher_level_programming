#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for item in dir(hidden_4):
        if item.find('_', end = 1) != -1:
            continue
        print("{}".format(item))
