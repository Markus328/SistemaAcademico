import bd
#!/usr/bin/env python
import cgitb,cgi
cgitb.enable(display = 0, logdir = "./")
form = cgi.FieldStorage()

from flask import *

def professor():
    var = 1 + 1
    return render_template('professor.py', valor=var)

usuario = int (form.getvalue('usuario'))
senha =  (form.getvalue('senha'))

bd.connect("banco de dados")
bd.select("login_matricula", "professor")
matriculaProfessor = []
matriculaProfessor.append(bd.cursor.fetchall())

bd.select("senha", "professor")
senhaProfessor = []
senhaProfessor.append(bd.cursor.fetchall())
i = -1
int(i)
while(i <= len(senhaProfessor)):
    i=i+1
    if usuario == matriculaProfessor[i]:
        j=-1
        int(j)
        while(j <= len(senhaProfessor)):
            j=j+1
            if senha == senhaProfessor[i]:
               professor()
    else:
        print("<h0.5>SENHA OU MATRICULA INCORRETOS <h0.5>")