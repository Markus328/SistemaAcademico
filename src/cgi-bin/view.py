import cgi
import os

form = cgi.FieldStorage()

def __join_args(args):
    text = ""
    for e in args:
        text += str(e)
    return text

def init():
    print("Content-type:text/html\n\n")

def start():
    print("<html>")
    print("<body>")

def load(path):
    pdir = os.path.dirname(os.path.dirname(__file__))
    file : str
    with open(pdir + '/' + path) as f:
        file = f.read()
        f.close()
    return file

def display(*args):
    text = __join_args(args)
    print("<p>{}".format(text))

def display_b(*args):
    text = __join_args(args)
    print("<h1>{}</h1>".format(text))

def get_form(field):
    return form.getvalue(field)

def end():
    print("</body>")
    print("</html>")


