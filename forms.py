from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField

class FilterForm(FlaskForm):
    submit = SubmitField(label="Filter")
    cbxs = SelectMultipleField(label="Categories", choices=[])
    def __init__(self, clist):
        super().__init__()
        self.cbxs.choices = clist
