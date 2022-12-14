import bd
#!/usr/bin/env python
import cgitb,cgi
cgitb.enable(display = 0, logdir = "./")
form = cgi.FieldStorage()

from flask import *

def aluno():
    var = 1 + 1
    return render_template('aluno.py', valor=var)

usuario = int (form.getvalue('usuario'))
senha =  (form.getvalue('senha'))

bd.connect("banco de dados")
bd.select("login_matricula", "alunos")
matriculaAluno = []
matriculaAluno.append(bd.cursor.fetchall())

bd.select("senha", "alunos")
senhaAluno = []
senhaAluno.append(bd.cursor.fetchall())
i = -1
int(i)
while(i <= len(senhaAluno)):
    i=i+1
    if usuario == matriculaAluno[i]:
        j=-1
        int(j)
        while(j <= len(senhaAluno)):
            j=j+1
            if senha == senhaAluno[i]:
               aluno()
    else:
        print("<h0.5>SENHA OU MATRICULA INCORRETOS <h0.5>")


