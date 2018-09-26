import configparser
import mysql.connector

credential = configparser.ConfigParser()
credential.read('credential.conf')
hostname = credential.get('Credential', 'hostname')
username = credential.get('Credential', 'username')
password = credential.get('Credential', 'password')
database = credential.get('Credential', 'database')
db = mysql.connector.connect(host=hostname, user=username, passwd=password, database=database)
cursor = db.cursor()


def display_table(table_name):
    cursor.execute('SELECT * FROM ' + table_name)
    result = cursor.fetchall()

    if result:
        for row in result:
            print(row)
    else:
        print('Table ' + table_name + ' is empty.')


def add_item(shoe, table_name):
    sql_statement = 'INSERT INTO ' + table_name + ' (Name, Color, Size, Purchased_Price, Sold_Price)' + \
                    'VALUES (%s, %s, %s, %s, %s)'
    values = (shoe.name, shoe.color, shoe.size, shoe.purchased_price, shoe.sold_price)
    cursor.execute(sql_statement, values)
    db.commit()
    print(cursor.rowcount, 'record inserted')
