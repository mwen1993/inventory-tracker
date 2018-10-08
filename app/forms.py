from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, optional


class AddForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    size = IntegerField('Size', validators=[DataRequired()])
    purchased = IntegerField('Purchased Price', validators=[DataRequired()])
    sold = IntegerField('Sold Price (Optional)', validators=[optional()])
    submit = SubmitField('Add')


class DeleteForm(FlaskForm):
    item_id = IntegerField('ID of Item', validators=[DataRequired()])
    submit = SubmitField('Delete')


class UpdateForm(FlaskForm):
    Id = IntegerField('Id', validators=[DataRequired()])
    Name = StringField('Name', validators=[optional()])
    Color = StringField('Color', validators=[optional()])
    Size = IntegerField('Size', validators=[optional()])
    Purchased_Price = IntegerField('Purchased_Price', validators=[optional()])
    Sold_Price = IntegerField('Sold_Price', validators=[optional()])
    submit = SubmitField('Update')
