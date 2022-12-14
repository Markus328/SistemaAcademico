import bd
#!/usr/bin/env python
import cgitb,cgi
cgitb.enable(display = 0, logdir = "./")
form = cgi.FieldStorage()

bd.connect("banco de dados")
bd.select("nome", "disciplina")

disciplina = []
disciplina.append(bd.cursor.fetchall())

bd.select("nota", "alunos_has_disciplina")
nota = []
nota.append(bd.cursor.fetchall())

bd.select("presenca", "alunos_has_disciplina")
presenca = []
presenca.append(bd.cursor.fetchall())

print(""" <!DOCTYPE html>
<html lang="en">
<head>
    <link rel="icon" href="img5.png">
    <link rel="stylesheet" href="ui.css">
    <meta charset="UTF-8">
    <title>Aluno</title>
</head>
<body>


        

    <h1>Sistema Acadêmico Para Alunos</h1>

    <hr>

    <h2>Suas Notas e Frequências</h2>

        <div class="wrap-table100">
            <div class="table100 ver1">

            <div class="wrap-table100-nextcols js-pscroll ps ps--active-x">
            <div class="table100-nextcols">
            <table>
                
            <thead>
            <tr class="row100 head">
            <th class="cell100 column2">Disciplina</th>
            <th class="cell100 column3">Nota</th>
            <th class="cell100 column4">Frequência</th>

            </tr>
            </thead>

            <tbody>
            <tr class="row100 body">
            <td class="cell100 column2"> %s </td>
            <td class="cell100 column3"> %.2f </td>
            <td class="cell100 column4"> %d </td>


             <tr class="row100 body">
            <td class="cell100 column2"> %s </td>
            <td class="cell100 column3"> %.2f </td>
            <td class="cell100 column4"> %d </td>

            </tbody>
            </table>
            </div>
            <div class="ps__rail-x" style="width: 1165px; left: 0px; bottom: 10px;"><div class="ps__thumb-x" tabindex="0" style="left: 0px; width: 687px;"></div></div><div class="ps__rail-y" style="top: 0px; right: 0px;"><div class="ps__thumb-y" tabindex="0" style="top: 0px; height: 0px;"></div></div></div>
            </div>
            </div>

    <br>
    <br>

    <hr>


        <address>
            ©2022 Sistema Acadêmico
            <br>
            Sistema Acadêmico criado por Matheus Cristian, Abimael Ferreira, Abraão Rodrigues, Davi Ribeiro, Isaac Mota.
        </address>

</body>
</html>"""% (disciplina[0],nota[0],presenca[0],disciplina[1],nota[1],presenca[1]))