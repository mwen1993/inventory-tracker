from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, optional


class AddForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    size = IntegerField('Size', validators=[DataRequired()])
    purchased = IntegerField('Purchased Price', validators=[DataRequired()])
    sold = IntegerField('Sold Price', validators=[optional()])
    submit = SubmitField('Add')


class DeleteForm(FlaskForm):
    item_id = IntegerField('ID of Item', validators=[DataRequired()])
    submit = SubmitField('Delete')