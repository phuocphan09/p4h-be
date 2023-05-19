import contextlib
import sys
from io import StringIO
import traceback


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def runPythonCode(pythonCode):
    with stdoutIO() as s:
        try:
            exec(pythonCode)
        except Exception as e:
            return e
    return s.getvalue()


def runPythonCode2(cmd, globals=None, locals=None):
    hasError = True
    with stdoutIO() as s:
        try:
            exec(cmd, globals, locals)
        except SyntaxError as err:
            error_class = err.__class__.__name__
            detail = err.args[0]
            line_number = err.lineno

        except Exception as err:
            error_class = err.__class__.__name__
            detail = err.args[0]
            cl, exc, tb = sys.exc_info()
            # line_number = traceback.extract_tb(tb)[-1][1] # from stackoverflow https://stackoverflow.com/questions/28836078/how-to-get-the-line-number-of-an-error-from-exec-or-execfile-in-python
            line_number = traceback.extract_tb(tb)[1][1]
        else:
            hasError = False

    if not hasError:
        return s.getvalue()
    s.close()

    return {"error_class": error_class, "lineno": line_number, "detail": detail}


def runPythonCode3(cmd, globals=None, locals=None):
    hasError = True
    g = {}
    with stdoutIO() as s:
        try:
            exec(cmd, g, locals)
        except SyntaxError as err:
            error_detail = {"exception_info": err, "err_class": err.__class__.__name__, "detail": err.msg,
                            "line_no": [err.lineno, err.end_lineno], "char_no": [err.offset, err.end_offset],
                            "line_code": err.text}
        except Exception as err:
            cl, exc, tb = sys.exc_info()
            try:
                line_no = traceback.extract_tb(tb)[1][1]  # handle the out of index case
            except IndexError as e:
                line_no = 0
            error_detail = {"exception_info": err, "err_class": err.__class__.__name__, "detail": err.args[0],
                            "line_no": [line_no], "char_no": [], "full_traceback": traceback.extract_tb(tb)}
        else:
            hasError = False
    if not hasError:
        return s.getvalue()
    s.close()

    return error_detail
