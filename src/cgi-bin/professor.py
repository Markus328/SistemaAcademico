import bd
#!/usr/bin/env python
import cgitb,cgi
cgitb.enable(display = 0, logdir = "./")
form = cgi.FieldStorage()

bd.connect("banco de dados")
bd.select("nome", "alunos")

alunos = []
alunos.append(bd.cursor.fetchall())

bd.where("nota", "alunos_has_disciplina")
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
    <title>Professor</title>
</head>
<body>
    <h1>Sistema Acadêmico Para Professores</h1>

    <h2>Inserir notas e frequência dos alunos</h2>

    <div class="wrap-table100">
        <div class="table100 ver1">

        <div class="wrap-table100-nextcols js-pscroll ps ps--active-x">
        <div class="table100-nextcols">
        <table>
            
        <thead>
        <tr class="row100 head">
        <th class="cell100 column2">Nome do Aluno</th>
        <th class="cell100 column3">Nota</th>
        <th class="cell100 column4">Frequência</th>

        </tr>
        </thead>

        <tbody>
        <tr class="row100 body">
        <td class="cell100 column2">Matheus Cristian</td>
        <td class="cell100 column3">16 Nov 2012</td>
        <td class="cell100 column4">16 Nov 2017</td>


        </tr>
        <tr class="row100 body">
        <td class="cell100 column2">Abimael Ferreira</td>
        <td class="cell100 column3">16 Nov 2015</td>
        <td class="cell100 column4">30 Nov 2017</td>

        
        </tr>
        <tr class="row100 body">
        <td class="cell100 column2">Abraão Rodrigues</td>
        <td class="cell100 column3">16 Nov 2013</td>
        <td class="cell100 column4">30 Nov 2017</td>

        </tr>

        <tr class="row100 body">
        <td class="cell100 column2">Davi Ribeiro</td>
        <td class="cell100 column3">16 Nov 2013</td>
        <td class="cell100 column4">30 Nov 2017</td>


        <tr class="row100 body">
        <td class="cell100 column2">Isaac Mota </td>
        <td class="cell100 column3">16 Nov 2016</td>
        <td class="cell100 column4">30 Nov 2017</td>

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
</html>""")