from operations import get_table, add_item, delete_item, update_item
from shoe import Shoe

"""
driver method for the program
testing
"""

#delete_item(4, 'shoes')
updates = {'Size': 7, 'Color': 'White'}
get_table('shoes')
update_item(3, updates, 'shoes')
get_table('shoes')
'''
shoe = Shoe('test', 'test', 7, 260, 425)
add_item(shoe, 'shoes')
get_table('shoes')
'''


