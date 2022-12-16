import bd
import view


def run(usuario):
    bd.connect("SistemaAcademico")
    bd.select("professor P,disciplina D","P.nome,D.nome","P.matricula = %s AND D.iddisciplina = P.disciplina_iddisciplina" % usuario)
    nome,disciplina = bd.fetchall()[0]
    bd.select("professor P,alunos A, disciplina D, alunos_has_disciplina AD", "A.nome,AD.nota,AD.presenca", "P.matricula = %s AND P.disciplina_iddisciplina = D.iddisciplina AND D.iddisciplina = AD.disciplina_iddisciplina AND AD.alunos_matricula = A.matricula" % (usuario))
    table = bd.fetchall()

    html = view.load("paginaProfessor.html")
    line = "<tr class=\"row100 body\"><td class=\"cell100 column2\">{}</td><td class=\"cell100 column3\">{}</td><td class=\"cell100 column4\">{}</td></tr>"
    t = ""
    for x in table:
        t += line.format(*x)

    print(html.format(nome,disciplina,t))

