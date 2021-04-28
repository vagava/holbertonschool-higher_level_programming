#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    directory = dir(hidden_4)
    for index in directory:
        if index[0] is not "_":
            print("{}".format(index))
