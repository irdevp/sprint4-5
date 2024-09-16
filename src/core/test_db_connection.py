import pymysql
import os
# Configurações do banco de dados


host =os.getenv('host')
port =os.getenv('port')
user = os.getenv('user')
password =os.getenv('senha')
db_name = os.getenv('db_name')

# Conectando ao banco de dados
connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db_name,
                             port=port)

# Verificar a conexão

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Versão do MySQL: {version[0]}")
finally:
    connection.close()
