import bd
import view

def run(usuario):
    bd.connect("SistemaAcademico")


    bd.select("alunos","nome","matricula = %s" % usuario)
    nome = bd.fetchall()[0][0]
    bd.select("alunos_has_disciplina AD,disciplina D", "D.nome,AD.nota,AD.presenca", "AD.alunos_matricula = %s AND AD.disciplina_iddisciplina = D.iddisciplina" % (usuario))
    table = bd.fetchall()
    html = view.load("paginaAluno.html")
    line = "<tr class=\"row100 body\"><td class=\"cell100 column2\">{}</td><td class=\"cell100 column3\">{}</td><td class=\"cell100 column4\">{}</td></tr>" 
    t = ""
    for x in table:
       t += line.format(*x) 
        
    print(html.format(nome,t))
    
