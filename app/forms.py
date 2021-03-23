from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, SelectField, TextAreaField, DecimalField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description  = TextAreaField(u'Description')
    nobed = IntegerField('No. of Rooms', validators=[DataRequired()])
    nobath = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    property_type = SelectField(u'Property Type', choices=[('house', 'House'), ('ap', 'Apartment')])
    photo = FileField('Photo', validators=[
    		FileRequired(),
    		FileAllowed(['jpg', 'png', 'Images only!'])
    ])
