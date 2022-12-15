#!/usr/bin/env python3
import bd
import view



def run(usuario):
    bd.connect("teste")


    bd.select("alunos_has_disciplina", "disciplina_iddisciplina", "alunos_matricula = " + usuario)
    bd.select("disciplina", "nome", "iddisciplina = " + str(bd.fetchall()[0]))
    disciplina = bd.fetchall()
    bd.select("alunos_has_disciplina", "nota", "alunos_matricula = " + usuario)
    nota = bd.fetchall()

    bd.select("alunos_has_disciplina", "presenca", "alunos_matricula = " + usuario)
    presenca = bd.fetchall()

    html = view.load("paginaAluno.html") % (disciplina[0],nota[0],presenca[0])
    print(html)
