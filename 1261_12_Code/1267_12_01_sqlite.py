import sqlite3
connection = sqlite3.connect("mydb.db")
connection.execute(
        "CREATE TABLE IF NOT EXISTS "
        "pet (type, breed, gender, name)")
connection.execute("INSERT INTO pet VALUES("
        "'dog', 'spaniel', 'female', 'Esme')")
connection.execute("INSERT INTO pet VALUES("
        "'cat', 'persian', 'male', 'Oscar')")
results = connection.execute("SELECT breed, name"
        " from pet where type='dog'")
for result in results:
    print(result[1])
connection.close()
