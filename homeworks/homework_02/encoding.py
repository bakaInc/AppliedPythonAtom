

def get_c1251(filename):
    try:
        f = open(filename, "r", encoding="cp1251")
        f.read(1)
        f.seek(0)
    except UnicodeError:
        return 0
    return f


def get_utf_8(filename):
    try:
        f = open(filename, "r", encoding="utf-8")
        f.read(1)
        f.seek(0)
    except UnicodeError:
        return 0
    return f


def get_utf_16(filename):
    try:
        f = open(filename, "r", encoding="utf-16")
        f.read(1)
        f.seek(0)
    except UnicodeError:
        return 0
    return f


def get_encodeFile(filename):
    try:
        f = get_utf_8(filename)
        if(f):
            return f
        else:
            f = get_utf_16(filename)
            if(f):
                return f
            else:
                f = get_c1251(filename)
                if(f):
                    return f
                else:
                    raise UnicodeError
    except FileNotFoundError:
        raise FileNotFoundError
