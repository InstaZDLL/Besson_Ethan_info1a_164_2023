from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired


class ModifyMaterielForm(FlaskForm):
    id_mat = StringField('ID', validators=[DataRequired()])
    nom_mat = StringField('Nom', validators=[DataRequired()])
    model_mat = StringField('Modèle', validators=[DataRequired()])
    serial_num = StringField('Numéro de série', validators=[DataRequired()])
    date_achat = DateTimeField('Date d\'achat', validators=[DataRequired()])
    date_expi = DateTimeField('Date d\'expiration', validators=[DataRequired()])
    prix_mat = StringField('Prix', validators=[DataRequired()])
    nom_cat = SelectField('Catégorie', choices=[], validators=[DataRequired()])
