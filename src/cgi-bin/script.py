import bd

bd.connect("test")
bd.insert("Persons",values='("Markus", 17)',columns="(name, age)")
bd.select("Persons", "*")
res = bd.cursor.fetchall()
if len(res) >= 5:
    bd.delete("Persons")

for x in res:
    print(x)
