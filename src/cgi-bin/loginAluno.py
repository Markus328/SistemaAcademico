#!/usr/bin/env python3
import bd
import view
import aluno

usuario = int(view.get_form('usuario'))
senha =  int(view.get_form('senha'))
bd.connect("teste")

bd.select("alunos", "matricula")
matriculaAluno = bd.fetchall()

bd.select("alunos","senha")
senhaAluno = bd.fetchall()
view.init()
for mat in matriculaAluno:
    if usuario == mat:
        for sen in senhaAluno:
            if senha == sen:
                aluno.run(str(usuario))
                exit()
        break


view.display_b("MATRICULA OU SENHA INCORRETOS")
