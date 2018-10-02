from prettytable import PrettyTable, from_db_cursor


def display_table(cursor):
    """
    using the cursor from the return of a database, display the all rows as a table
    :param cursor: DBCursor Object
        a cursor object used to iterate each row of a table return from the database
    :return:
    """
    table = from_db_cursor(cursor)
    print(table)


def print_options():
    table = PrettyTable(['Key', 'Options'])
    table.align = 'l'
    #table.border = False

    table.add_row(['1', 'Show available tables in database'])
    table.add_row(['2', 'Display a specific table'])
    table.add_row(['3', 'Add a new entry to a table'])
    table.add_row(['4', 'Update an existing entry in a table'])
    table.add_row(['5', 'Delete an entry in a table'])
    table.add_row(['0', 'Exit Application'])

    print(table)