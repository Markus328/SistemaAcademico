#!/usr/bin/env python3

import bd
import view
import aluno
import professor

usuario = view.get_form('usuario')
senha =  view.get_form('senha')
typ = view.get_form('type')

func = aluno.run
if typ == "professor":
    func = professor.run

bd.connect("SistemaAcademico")

bd.select(typ, "senha", "matricula = " + usuario)
senhaQuery = bd.fetchall()
view.init()
if len(senhaQuery) == 1:
    if senhaQuery[0][0] == int(senha):
        func(usuario)
        exit()

view.display_b("MATRICULA OU SENHA INCORRETAS")

