from flask import render_template, redirect, url_for, flash
from app import app
from operations import get_table, add_item, delete_item
from forms import AddForm, DeleteForm
from shoe import Shoe


@app.route('/')
@app.route('/index')
def index():
    add_form = AddForm()
    delete_form = DeleteForm()
    cursor = get_table('shoes')
    header = [x[0] for x in cursor.description]
    content = cursor.fetchall()
    return render_template('index.html', header=header, content=content, add_form=add_form, delete_form=delete_form)


@app.route('/add', methods=['POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        new_shoe = Shoe(form.name.data, form.color.data, form.size.data, form.purchased.data, form.sold.data)
        message = add_item(new_shoe, 'shoes')
        flash(message)
        return redirect(url_for('index'))
    else:
        flash('Item was not added, some of the data format is incorrect, please try again.')
        return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
    form = DeleteForm()
    print(form.item_id.data)
    if form.validate_on_submit():
        message = delete_item(str(form.item_id.data), 'shoes')
        flash(message)
        return redirect(url_for('index'))
    else:
        flash('Item was not deleted, some of the data format is incorrect, please try again.')
        return redirect(url_for('index'))
