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


def dwnld_zip(url, file="a.zip"):
    data = r.urlopen(url)
    f = open(file, "wb")
    f.write(data.read())
    print(url + " data written to file:" + os.getcwd() + "/" + file)


def word_in_list(data, word):
    """Checks if there is a string containing the word supplied and
    returns the list of those words.
    """
    if not hasattr(data, "__iter__"):
        print("Not a list/tuple!")
        return

    return [i for i in data if(word in i)]
