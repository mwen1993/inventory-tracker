from flask import render_template, redirect, url_for, flash
from app import app
from operations import get_table, add_item, delete_item, update_item
from forms import AddForm, DeleteForm, UpdateForm
from shoe import Shoe


@app.route('/')
@app.route('/index')
def index():
    add_form = AddForm()
    delete_form = DeleteForm()
    update_form = UpdateForm()
    header_row, content = get_table('shoes')
    header = [x[0] for x in header_row]
    return render_template('index.html', header=header, content=content,
                           add_form=add_form, delete_form=delete_form, update_form=update_form
                           )


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
    if form.validate_on_submit():
        message = delete_item(str(form.id.data), 'shoes')
        flash(message)
        return redirect(url_for('index'))
    else:
        flash('Item was not deleted, some of the data format is incorrect, please try again.')
        return redirect(url_for('index'))


@app.route('/update', methods=['POST'])
def update():
    form = UpdateForm()
    updates = {}
    if form.validate_on_submit():
        if form.Name.data != '':
            updates[form.Name.name] = form.Name.data
        if form.Color.data != '':
            updates[form.Color.name] = form.Color.data
        if form.Size.data is not None:
            updates[form.Size.name] = form.Size.data
        if form.Purchased_Price.data is not None:
            updates[form.Purchased_Price.name] = form.Purchased_Price.data
        if form.Sold_Price.data is not None:
            updates[form.Sold_Price.name] = form.Sold_Price.data
        if updates:
            message = update_item(str(form.Id.data), updates, 'shoes')
            flash(message)
            return redirect(url_for('index'))
        else:
            flash('There is nothing to be updated, please enter value for the column you wish to update.')
            return redirect(url_for('index'))
    else:
        flash('Please enter an Id of the item you wish to update with the correct column data type.')
        return redirect(url_for('index'))
