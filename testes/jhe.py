import oracledb
# Conexão 
connection = oracledb.connect(
    user = "BD150224212",
    password = 'Dsiow3',    
    dsn = "172.16.12.14/xe")
print("Successfully Connected")
cursor = connection.cursor()
for row in cursor.execute("SELECT * FROM estoque"):
    estoque = row
    print(estoque)