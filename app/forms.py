from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, optional


class AddForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    color = StringField(validators=[DataRequired()])
    size = IntegerField(validators=[DataRequired()])
    purchased = IntegerField(validators=[DataRequired()])
    sold = IntegerField(validators=[optional()])


class DeleteForm(FlaskForm):
    id = IntegerField('ID of Item', validators=[DataRequired()])


class UpdateForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    name = StringField('Name', validators=[optional()])
    color = StringField('Color', validators=[optional()])
    size = IntegerField('Size', validators=[optional()])
    purchased_price = IntegerField('Purchased_Price', validators=[optional()])
    sold_price = IntegerField('Sold_Price', validators=[optional()])
