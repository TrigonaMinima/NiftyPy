from pathlib import Path


Path.ls = lambda x: list(x.iterdir())


def shell(cmd):
    """
    Runs any shell command.
    """
    import os

    p = os.popen(cmd)
    res = p.readlines()
    p.close()

    return res


def ls(path=""):
    """
    Gives file listing.
    """
    if not path:
        path = "./"

    if not isinstance(path, Path):
        path = Path(path)

    paths = path.ls()
    print("\n".join(sorted([i.as_posix() for i in paths])))
    return paths

def dwnld_zip(url, file="a.zip"):
    data = r.urlopen(url)
    f = open(file, "wb")
    f.write(data.read())
    print(url + " data written to file:" + os.getcwd() + "/" + file)
