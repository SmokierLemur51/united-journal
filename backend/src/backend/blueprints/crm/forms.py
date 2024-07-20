from flask_wtf import FlaskForm

from wtforms import EmailField, StringField, SelectField
from wtforms.validators import DataRequired, Email

class CreateCustomer(FlaskForm):
    company = StringField(label="Company", validators=[DataRequired(message='Company name required.')])
    street = StringField(label="Street", validators=[DataRequired(message='Street address required.')])
    street2 = StringField(label="Street 2")
    city = StringField(label="City", validators=[DataRequired(message='City required.')])
    state = SelectField(label="State", validators[DataRequired(message='State required.')])
    zip_code = StringField(label="Zip Code", validators=[DataRequired(message='Zip code required.')])


class CreateContact(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message='Contact name required.')])
    phone = StringField(label='Phone', validators=[DataRequired(message='Phone number required.')])
    email = EmailField(label='Email', validators=[Email(message='Invalid email address.')])
    company = SelectField(label="Company")


