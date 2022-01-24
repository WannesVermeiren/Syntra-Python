import mysql.connector as mysql

def GetConfig():
    return {
        'user': 'root',
        'password': 'Sdf7539516556',
        'host': '127.0.0.1',
        'database': 'sakila',
        'raise_on_warnings': True
    }


def GetData(sql):
    config = GetConfig()
    connection = mysql.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)

    data = []
    for row in cursor:
        data.append(row)

    cursor.close()
    connection.close()
    return data

