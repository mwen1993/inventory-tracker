from app import credential
import mysql.connector
#from utils import display_table

hostname = credential.get('Credential', 'hostname')
username = credential.get('Credential', 'username')
password = credential.get('Credential', 'password')
database = credential.get('Credential', 'database')
db = mysql.connector.connect(host=hostname, user=username, passwd=password, database=database)
cursor = db.cursor()


def list_tables():
    """
    Output a list of all available tables in the database
    :return:
    """
    cursor.execute('SHOW tables')
    #display_table(cursor)


def get_table(table_name):
    """
    Selects the entire table and display it
    :param table_name: string
        the name of the table to display
    :return: None
    """
    cursor.execute('SELECT * FROM ' + table_name)

    return cursor


def add_item(shoe, table_name):
    """
    add a new item to a table
    :param shoe: Shoe Object
        a Shoe Object encapsulating all the required column data to be inputed into the database
    :param table_name: string
        name of the table
    :return: None
    """
    sql_statement = 'INSERT INTO ' + table_name + ' (Name, Color, Size, Purchased_Price, Sold_Price)' + \
                    'VALUES (%s, %s, %s, %s, %s)'
    values = (shoe.name, shoe.color, shoe.size, shoe.purchased_price, shoe.sold_price)

    try:
        cursor.execute(sql_statement, values)
        db.commit()
        return 'New entry has been added!'
    except Exception as e:
        return str(e)


def delete_item(item_id, table_name):
    """
    delete an item from the database corresponding to a unique id
    :param item_id: int
        the unique Id in the database corresponding to the item
    :param table_name: string
        name of the table
    :return: None
    """
    sql_statement = 'DELETE FROM ' + table_name + ' WHERE Id = ' + str(item_id)

    try:
        cursor.execute(sql_statement)
        db.commit()
        return 'Item ID: ' + item_id + ' has been deleted.'
    except Exception as e:
        print('inside exception for delete')
        return str(e)


def update_item(item_id, updates, table_name):
    """
    make an update to a single row in database given the item Id
    :param item_id: int
        the unique Id in the database corresponding to the item
    :param updates: dictionary
        contains key, value pairs,(column name:values) to be updated, each key is a column name and values is update val
    :param table_name: string
        name of the table
    :return: None
    """
    sql_statement = 'UPDATE ' + table_name + ' SET '

    for key, value in updates.items():
        if type(value) is int:
            sql_statement += key + ' = ' + str(value) + ', '
        else:

            sql_statement += key + ' = \'' + str(value) + '\', '

    sql_statement = sql_statement.rstrip(', ')
    sql_statement += ' WHERE Id = ' + str(item_id)

    cursor.execute(sql_statement)
    db.commit()
    print(cursor.rowcount, 'record(s) updated')
