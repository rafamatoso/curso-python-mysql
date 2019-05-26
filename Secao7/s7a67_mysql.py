import MySQLdb

# Configurações para conexão do MySQL

host = 
user = 
password = 
db = 
port = 

# Executa a conexão

con = MySQLdb.connect(host, user, password, db, port)

# Cria um cursor no qual as consultas podem ser realizadas

c = con.cursor(MySQLdb.cursors.DictCursor)

def select (fields, tables, where = None):

    global c # c será uma variável global, podendo ser usada internamente na função

    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where

    c.execute(query)

    return c.fetchall()

#result = select("nome, cpf", "alunos")

#print(result)

'''for i in result:
    print(str(i))'''

def insert(values, table, fields=None):

    global c, con

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()

'''values = [
    "'NULL', 'Melissa Gouveia', '1989-06-24', 'Av. Olinda, 125', 'OLINDA', 'PE', '78412546932'",
    "'NULL', 'Igor Nascimento', '1992-08-11', 'Rua do Imperador, 425', 'RECIFE', 'PE', '14521563587'"]'''

#insert(values, "alunos")

#result2 = select("*", "alunos")

'''for i in result2:
    print(str(i))'''

def update(sets, table, where=None):

    global c, con

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    con.commit()

#update({"nome":"João Martins", "cidade":"CABO"}, "alunos", "id_aluno = 8")
#print(select("*", "alunos", "id_aluno = 8"))

def delete(table, where):

    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()

#print(select("*", "alunos", "id_aluno = 9"))
#print(delete("alunos", "id_aluno = 9"))
#print(select("*", "alunos", "id_aluno = 9"))