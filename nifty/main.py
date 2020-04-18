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


def set_highlighted_excepthook():
    import sys
    import traceback
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import TerminalFormatter

    lexer = get_lexer_by_name(
        "pytb" if sys.version_info.major < 3 else "py3tb")
    formatter = TerminalFormatter()

    def myexcepthook(type, value, tb):
        tbtext = ''.join(traceback.format_exception(type, value, tb))
        sys.stderr.write(highlight(tbtext, lexer, formatter))

    sys.excepthook = myexcepthook
