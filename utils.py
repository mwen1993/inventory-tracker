from prettytable import PrettyTable, from_db_cursor


def display_table(header_row, data_rows):

    table = PrettyTable([x[0] for x in header_row])
    table.align['Name'] = 'l'
    table.align['Color'] = 'l'
    table.align['Purchased_Price'] = 'r'
    table.align['Sold_Price'] = 'r'

    for row in data_rows:
        table.add_row(row)

    print(table)
