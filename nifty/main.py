import os
from urllib import request as r

# run1 = lambda x: exec(open(x).read())


# def run2(x):
#     exec(open(x).read(), locals())


def shell(cmd):
    """Runs any shell command.
    """
    p = os.popen(cmd)
    res = p.readlines()
    p.close()

    return res


def ls(flag=""):
    """Gives file listing. "flag" is the linux ls command options.
    """
    return shell("ls" + flag)


def freq(iterable):
    """Frequency analysis of any hashable iterable.
    """
    freq_table = {}
    for i in iterable:
        freq_table[i] = freq_table.get(i, 0) + 1

    return freq_table


def dwnld(url, file="a.zip"):
    data = r.urlopen(url)
    f = open(file, "wb")
    f.write(data.read())
    print(url + " data written to file:" + os.getcwd() + "/" + file)
