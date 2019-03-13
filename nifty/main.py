import os

from pathlib import Path


Path.ls = lambda x: list(x.iterdir())


def shell(cmd):
    """
    Runs any shell command.
    """
    p = os.popen(cmd)
    res = p.readlines()
    p.close()

    return res


def ls(path=""):
    """
    Gives file listing.
    """
    from pathlib import Path

    if path:
        return Path(path).ls()
    else:
        return Path("./").ls()


def dwnld_zip(url, file="a.zip"):
    data = r.urlopen(url)
    f = open(file, "wb")
    f.write(data.read())
    print(url + " data written to file:" + os.getcwd() + "/" + file)
